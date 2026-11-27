#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""火山引擎机器翻译（TranslateText）。

用法:
    python scripts/volc_translate.py "标题"
    python scripts/volc_translate.py "标题" --snake

环境变量:
    VOLCENGINE_ACCESS_KEY_ID / VOLCENGINE_SECRET_ACCESS_KEY
    兼容: VOLCENGINE_AK / VOLCENGINE_SK
    VOLCENGINE_REGION（可选，默认 cn-north-1）
    VOLCENGINE_SESSION_TOKEN（可选，临时凭证时使用）
"""

import argparse
import hashlib
import hmac
import json
import os
import re
import sys
import unicodedata
from datetime import datetime, timezone
from urllib.parse import quote

try:
    import requests
except ImportError:
    requests = None

HOST = "translate.volcengineapi.com"
SERVICE = "translate"
ACTION = "TranslateText"
VERSION = "2020-06-01"
DEFAULT_REGION = "cn-north-1"

AK_NAMES = (
    "VOLCENGINE_ACCESS_KEY_ID",
    "VOLCENGINE_AK",
    "VOLC_ACCESS_KEY_ID",
    "VOLC_AK",
    "VOLC_ACCESS_KEY",
    "VOLC_ACCESSKEY",
    "VOLCENGINE_ACCESS_KEY",
    "VOLCENGINE_ACCESSKEY",
)
SK_NAMES = (
    "VOLCENGINE_SECRET_ACCESS_KEY",
    "VOLCENGINE_SK",
    "VOLC_SECRET_ACCESS_KEY",
    "VOLC_SK",
    "VOLC_SECRET_KEY",
    "VOLC_SECRETKEY",
    "VOLCENGINE_SECRET_KEY",
    "VOLCENGINE_SECRETKEY",
)


class VolcTranslateError(RuntimeError):
    pass


def _env(names):
    for name in names:
        value = os.environ.get(name)
        if value:
            return value
    return ""


def credentials():
    ak = _env(AK_NAMES)
    sk = _env(SK_NAMES)
    if not ak or not sk:
        raise VolcTranslateError(
            "未设置火山引擎密钥：VOLCENGINE_ACCESS_KEY_ID / "
            "VOLCENGINE_SECRET_ACCESS_KEY"
        )
    return ak, sk


def _encode(value):
    return quote(str(value), safe="-_.~")


def canonical_query(params):
    return "&".join(
        f"{_encode(key)}={_encode(value)}" for key, value in sorted(params.items())
    )


def _hmac(key, content):
    return hmac.new(key, content.encode("utf-8"), hashlib.sha256).digest()


def _sha256(content):
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def snake_case(text):
    value = unicodedata.normalize("NFKD", text or "")
    value = value.encode("ascii", "ignore").decode("ascii")
    value = re.sub(r"[^a-zA-Z0-9]+", "_", value).strip("_").lower()
    return re.sub(r"_+", "_", value)


def translate_text(text, target="en", source=None, timeout=20):
    if not text or not text.strip():
        return ""
    if requests is None:
        raise VolcTranslateError("缺少 requests，请先安装：pip install requests")

    ak, sk = credentials()
    region = os.environ.get("VOLCENGINE_REGION", DEFAULT_REGION)
    session_token = os.environ.get("VOLCENGINE_SESSION_TOKEN", "")

    now = datetime.now(timezone.utc)
    x_date = now.strftime("%Y%m%dT%H%M%SZ")
    short_date = x_date[:8]
    content_type = "application/json"

    body = {
        "TargetLanguage": target,
        "TextList": [text],
    }
    if source:
        body["SourceLanguage"] = source
    payload = json.dumps(body, ensure_ascii=False)

    x_content_sha256 = _sha256(payload)
    query = {"Action": ACTION, "Version": VERSION}
    query_string = canonical_query(query)

    headers_to_sign = [
        ("content-type", content_type),
        ("host", HOST),
        ("x-content-sha256", x_content_sha256),
        ("x-date", x_date),
    ]
    if session_token:
        headers_to_sign.append(("x-security-token", session_token))
    headers_to_sign.sort(key=lambda item: item[0])

    signed_headers = ";".join(name for name, _ in headers_to_sign)
    canonical_headers = "".join(f"{name}:{value}\n" for name, value in headers_to_sign)
    canonical_request = "\n".join(
        [
            "POST",
            "/",
            query_string,
            canonical_headers,
            signed_headers,
            x_content_sha256,
        ]
    )

    credential_scope = f"{short_date}/{region}/{SERVICE}/request"
    string_to_sign = "\n".join(
        ["HMAC-SHA256", x_date, credential_scope, _sha256(canonical_request)]
    )

    k_date = _hmac(sk.encode("utf-8"), short_date)
    k_region = _hmac(k_date, region)
    k_service = _hmac(k_region, SERVICE)
    k_signing = _hmac(k_service, "request")
    signature = hmac.new(
        k_signing, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    authorization = (
        f"HMAC-SHA256 Credential={ak}/{credential_scope}, "
        f"SignedHeaders={signed_headers}, Signature={signature}"
    )

    headers = {
        "Content-Type": content_type,
        "Host": HOST,
        "X-Date": x_date,
        "X-Content-Sha256": x_content_sha256,
        "Authorization": authorization,
    }
    if session_token:
        headers["X-Security-Token"] = session_token

    url = f"https://{HOST}/?{query_string}"
    try:
        response = requests.post(
            url, headers=headers, data=payload.encode("utf-8"), timeout=timeout
        )
    except Exception as exc:
        raise VolcTranslateError(f"请求失败：{exc}") from exc

    try:
        data = response.json()
    except ValueError as exc:
        raise VolcTranslateError(
            f"响应不是 JSON（HTTP {response.status_code}）：{response.text[:200]}"
        ) from exc

    meta = data.get("ResponseMetadata") or {}
    error = meta.get("Error")
    if error:
        raise VolcTranslateError(
            f"{error.get('Code', 'Error')}: {error.get('Message', '')}"
        )

    items = data.get("TranslationList") or []
    if not items or not items[0].get("Translation"):
        raise VolcTranslateError(f"未返回翻译结果：{json.dumps(data, ensure_ascii=False)}")

    return items[0]["Translation"]


def main():
    parser = argparse.ArgumentParser(description="火山引擎机器翻译")
    parser.add_argument("text", nargs="+", help="待翻译文本")
    parser.add_argument("--target", default="en", help="目标语言，默认 en")
    parser.add_argument("--source", default="", help="源语言，留空自动检测")
    parser.add_argument("--snake", action="store_true", help="同时输出蛇形命名")
    args = parser.parse_args()

    text = " ".join(args.text)
    try:
        translated = translate_text(text, args.target, args.source or None)
    except VolcTranslateError as exc:
        print(f"翻译失败：{exc}", file=sys.stderr)
        return 1

    print(translated)
    if args.snake:
        print(snake_case(translated))
    return 0


if __name__ == "__main__":
    sys.exit(main())

# -*- coding: utf-8 -*-
"""腾讯云机器翻译脚本（TextTranslate: zh -> en）。

用法:
    python3 transfer.py "<待翻译文本>"

需要环境变量:
    TENCENTCLOUD_SECRET_ID
    TENCENTCLOUD_SECRET_KEY
"""
import hashlib
import hmac
import json
import os
import sys
import time
from datetime import datetime, timezone

import requests  # pip3 install requests


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def main():
    if len(sys.argv) < 2:
        print(f"用法: {sys.argv[0]} <待翻译文本>")
        raise SystemExit(1)

    origin = sys.argv[1]
    print("待翻译文本：", origin)

    # 设置环境变量
    secret_id = os.environ.get("TENCENTCLOUD_SECRET_ID")
    secret_key = os.environ.get("TENCENTCLOUD_SECRET_KEY")

    # 检查密钥是否存在
    if not secret_id or not secret_key:
        raise ValueError("请设置环境变量 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY")

    # API 参数
    service = "tmt"  # 服务名称（机器翻译）
    host = f"{service}.tencentcloudapi.com"
    endpoint = f"https://{host}"
    region = "ap-guangzhou"
    action = "TextTranslate"  # 接口名称
    version = "2018-03-21"  # API 版本
    algorithm = "TC3-HMAC-SHA256"
    timestamp = int(time.time())
    date = datetime.fromtimestamp(timestamp, tz=timezone.utc).strftime("%Y-%m-%d")

    # 请求参数
    params = {
        "SourceText": origin,   # 待翻译的文本
        "Source": "zh",         # 源语言代码（中文）
        "Target": "en",         # 目标语言代码（英语）
        "ProjectId": 0          # 项目 ID
    }

    # ************* 步骤 1：拼接规范请求串 *************
    http_request_method = "POST"
    canonical_uri = "/"
    canonical_querystring = ""
    ct = "application/json; charset=utf-8"
    payload = json.dumps(params, ensure_ascii=False)
    canonical_headers = f"content-type:{ct}\nhost:{host}\nx-tc-action:{action.lower()}\n"
    signed_headers = "content-type;host;x-tc-action"
    hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    canonical_request = (http_request_method + "\n" +
                         canonical_uri + "\n" +
                         canonical_querystring + "\n" +
                         canonical_headers + "\n" +
                         signed_headers + "\n" +
                         hashed_request_payload)

    # ************* 步骤 2：拼接待签名字符串 *************
    credential_scope = date + "/" + service + "/" + "tc3_request"
    hashed_canonical_request = hashlib.sha256(
        canonical_request.encode("utf-8")
    ).hexdigest()
    string_to_sign = (algorithm + "\n" +
                      str(timestamp) + "\n" +
                      credential_scope + "\n" +
                      hashed_canonical_request)

    # ************* 步骤 3：计算签名 *************
    secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
    secret_service = sign(secret_date, service)
    secret_signing = sign(secret_service, "tc3_request")
    signature = hmac.new(
        secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()

    # ************* 步骤 4：拼接 Authorization *************
    authorization = (algorithm + " " +
                     "Credential=" + secret_id + "/" + credential_scope + ", " +
                     "SignedHeaders=" + signed_headers + ", " +
                     "Signature=" + signature)

    # ************* 步骤 5：发送请求 *************
    headers = {
        "Authorization": authorization,
        "Content-Type": "application/json; charset=utf-8",
        "Host": host,
        "X-TC-Action": action,
        "X-TC-Timestamp": str(timestamp),
        "X-TC-Version": version,
        "X-TC-Region": region
    }

    response = requests.post(endpoint, headers=headers, data=payload, timeout=30)

    # 输出结果
    if response.status_code == 200:
        response_data = response.json()

        # 腾讯云 API 出错时返回 200 + Response.Error
        resp = response_data.get("Response", {})
        if "Error" in resp:
            err = resp["Error"]
            print("API 错误:", err.get("Code"), err.get("Message"))
            raise SystemExit(1)

        translated_text = resp["TargetText"]
        print("翻译结果：", translated_text)

        # 替换空格并打印（可直接用作 slug）
        replaced_text = translated_text.replace(" ", "_")
        print("替换后的结果：", replaced_text)
    else:
        print("请求失败，状态码：", response.status_code)
        print("错误信息：", response.text)
        raise SystemExit(1)


if __name__ == "__main__":
    main()

# //==========================================================
# // 文件名: tencloud.py
# // 作者: simons
# // 邮箱: reggiesimons2cy@gmail.com
# // 创建时间: Sat Jan 25 06:16:48 2025
# //==========================================================
# -*- coding: utf-8 -*-
"""腾讯云 TC3 签名演示脚本（机器翻译 TextTranslate）。

需要环境变量:
    TENCENTCLOUD_SECRET_ID
    TENCENTCLOUD_SECRET_KEY
"""
import hashlib
import hmac
import json
import os
import time
from datetime import datetime, timezone


def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()


def main():
    secret_id = os.environ.get("TENCENTCLOUD_SECRET_ID")
    secret_key = os.environ.get("TENCENTCLOUD_SECRET_KEY")
    if not secret_id or not secret_key:
        raise SystemExit(
            "请设置环境变量 TENCENTCLOUD_SECRET_ID 和 TENCENTCLOUD_SECRET_KEY"
        )

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
        "SourceText": "hello",  # 待翻译的文本
        "Source": "en",         # 源语言代码（英语）
        "Target": "zh",         # 目标语言代码（中文）
        "ProjectId": 0          # 项目 ID
    }

    # ************* 步骤 1：拼接规范请求串 *************
    http_request_method = "POST"
    canonical_uri = "/"
    canonical_querystring = ""
    ct = "application/json; charset=utf-8"
    payload = json.dumps(params, ensure_ascii=False)
    canonical_headers = (
        "content-type:%s\nhost:%s\nx-tc-action:%s\n" % (ct, host, action.lower())
    )
    signed_headers = "content-type;host;x-tc-action"
    hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
    canonical_request = (http_request_method + "\n" +
                         canonical_uri + "\n" +
                         canonical_querystring + "\n" +
                         canonical_headers + "\n" +
                         signed_headers + "\n" +
                         hashed_request_payload)
    print("[debug] canonical_request:\n", canonical_request)

    # ************* 步骤 2：拼接待签名字符串 *************
    credential_scope = date + "/" + service + "/" + "tc3_request"
    hashed_canonical_request = hashlib.sha256(
        canonical_request.encode("utf-8")
    ).hexdigest()
    string_to_sign = (algorithm + "\n" +
                      str(timestamp) + "\n" +
                      credential_scope + "\n" +
                      hashed_canonical_request)
    print("[debug] string_to_sign:\n", string_to_sign)

    # ************* 步骤 3：计算签名 *************
    secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
    secret_service = sign(secret_date, service)
    secret_signing = sign(secret_service, "tc3_request")
    signature = hmac.new(
        secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256
    ).hexdigest()
    print("[debug] signature:", signature)

    # ************* 步骤 4：拼接 Authorization（不直接打印完整凭证） *************
    authorization = (algorithm + " " +
                     "Credential=" + secret_id + "/" + credential_scope + ", " +
                     "SignedHeaders=" + signed_headers + ", " +
                     "Signature=" + signature)

    # 输出可复用的 curl 命令（Authorization 已脱敏，运行时请自行替换）
    print("\n可复制的 curl 命令模板（Authorization 需运行时注入，勿提交到仓库）:")
    print('curl -X POST ' + endpoint
          + ' -H "Authorization: $TC_AUTHORIZATION"'
          + ' -H "Content-Type: application/json; charset=utf-8"'
          + ' -H "Host: ' + host + '"'
          + ' -H "X-TC-Action: ' + action + '"'
          + ' -H "X-TC-Timestamp: ' + str(timestamp) + '"'
          + ' -H "X-TC-Version: ' + version + '"'
          + ' -H "X-TC-Region: ' + region + '"'
          + " -d '" + payload + "'")
    print("\n签名计算成功（Authorization 含凭证，已省略打印）")


if __name__ == "__main__":
    main()

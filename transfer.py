# -*- coding: utf-8 -*-
import hashlib
import hmac
import json
import os
import time
from datetime import datetime
import requests  # 导入 requests 库
import sys

# 获取命令行参数
args = sys.argv

# 输出脚本名称
print("脚本名称：", args[0])

origin = "草稿文件"

# 输出其他参数
if len(args) > 1:
    print("参数列表：", args[1:])
    origin = args[1]

else:
    print("未提供参数。")


# origin  = "草稿文件"
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
timestamp = int(time.time())  # 动态生成时间戳
date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")

# 请求参数
params = {
    "SourceText": origin,  # 待翻译的文本
    "Source": "zh",         # 源语言代码（英语）
    "Target": "en",         # 目标语言代码（中文）
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
hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
string_to_sign = (algorithm + "\n" +
                  str(timestamp) + "\n" +
                  credential_scope + "\n" +
                  hashed_canonical_request)

# ************* 步骤 3：计算签名 *************
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()

secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
secret_service = sign(secret_date, service)
secret_signing = sign(secret_service, "tc3_request")
signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()

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

# 发送 POST 请求
response = requests.post(endpoint, headers=headers, data=payload)

# 输出结果
if response.status_code == 200:
    response_data = response.json()
    print(response_data)
    print("翻译结果：", response_data['Response']['TargetText'])
else:
    print("请求失败，状态码：", response.status_code)
    print("错误信息：", response.text)

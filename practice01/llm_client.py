import os
import json
import http.client
from urllib.parse import urlparse
from dotenv import load_dotenv

# 加载 .env
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
MODEL_NAME = os.getenv("MODEL_NAME")
API_TOKEN = os.getenv("API_TOKEN")

print(f"BASE_URL = {BASE_URL}")
print(f"MODEL_NAME = {MODEL_NAME}")
print(f"API_TOKEN = {API_TOKEN}")

if not BASE_URL or not MODEL_NAME:
    print("错误：请在 .env 文件中正确配置 BASE_URL 和 MODEL_NAME")
    exit(1)

try:
    parsed = urlparse(BASE_URL)
    if parsed.scheme == "http":
        conn = http.client.HTTPConnection(parsed.netloc)
    else:
        conn = http.client.HTTPSConnection(parsed.netloc)

    payload = {
        "model": MODEL_NAME,
        "messages": [{"role": "user", "content": "uesr:你好，我叫肖中林。\nai:您好，肖中林先生！很高兴能为您服务。请问有什么我可以帮您解答或处理 的吗？或者，如果您想聊聊最近的兴趣爱好、工作或者其他话题，也欢迎与 我说说。\n请问我叫什么名字？"}],
        "temperature": 1.5
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    print("正在发送请求...")
    conn.request("POST", "/v1/chat/completions", body=json.dumps(payload), headers=headers)
    resp = conn.getresponse()
    print(f"响应状态码: {resp.status}")

    data = json.loads(resp.read().decode())
    print("模型回答：")
    print(data['choices'][0]['message']['content'])

except Exception as e:
    print(f"发生错误: {e}")

finally:
    conn.close()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import json
import http.client
from urllib.parse import urlparse
from dotenv import load_dotenv
import time
import sys

# 强制设置UTF-8编码
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')

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

def get_connection():
    parsed = urlparse(BASE_URL)
    if parsed.scheme == "http":
        return http.client.HTTPConnection(parsed.netloc)
    else:
        return http.client.HTTPSConnection(parsed.netloc)

def send_request(messages):
    conn = get_connection()
    
    payload = {
        "model": MODEL_NAME,
        "messages": messages,
        "temperature": 1.0,
        "stream": True
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_TOKEN}"
    }

    try:
        conn.request("POST", "/v1/chat/completions", body=json.dumps(payload), headers=headers)
        return conn.getresponse()
    except Exception as e:
        print(f"发生错误: {e}")
        conn.close()
        return None

def handle_streaming_response(response):
    if not response:
        return ""
    
    full_response = ""
    print("\nAI: ", end="")
    
    try:
        while True:
            chunk = response.read(1024)
            if not chunk:
                break
            
            chunk_str = chunk.decode('utf-8')
            lines = chunk_str.split('\n')
            
            for line in lines:
                line = line.strip()
                if line.startswith('data:'):
                    data_part = line[5:].strip()
                    if data_part == '[DONE]':
                        break
                    try:
                        data = json.loads(data_part)
                        if 'choices' in data and data['choices']:
                            delta = data['choices'][0].get('delta', {})
                            if 'content' in delta:
                                content = delta['content']
                                print(content, end="", flush=True)
                                full_response += content
                    except json.JSONDecodeError:
                        pass
    finally:
        response.close()
    
    print()  # 换行
    return full_response

def main():
    print("=====================================")
    print("         终端聊天界面")
    print("=====================================")
    print("输入消息与AI对话，按Ctrl+C退出")
    print("=====================================\n")
    
    # 初始化聊天历史
    chat_history = []
    
    try:
        while True:
            # 获取用户输入
            user_input = input("你: ")
            
            # 添加用户消息到历史
            chat_history.append({"role": "user", "content": user_input})
            
            # 发送请求并处理流式响应
            response = send_request(chat_history)
            if response:
                ai_response = handle_streaming_response(response)
                # 添加AI回复到历史
                chat_history.append({"role": "assistant", "content": ai_response})
            
            print()  # 空行分隔
    
    except KeyboardInterrupt:
        print("\n\n聊天结束，再见！")
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    main()
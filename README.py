"""
项目 README - Python 学习项目说明文档
==========================================

本文件用于记录项目中各个 Python 代码的功能用途及实现的教学目标。

---

项目结构
========

├── practice01/             # 第一个教学实践
│   └── llm_client.py       # 基础 LLM API 调用
├── practice02/             # 第二个教学实践  
│   ├── chat_interface.py   # 终端聊天界面（支持流式输出和历史记录）
│   └── tool_calling.py     # 工具调用系统（文件操作功能）
├── test.py                 # 基础测试文件
├── .env                    # 环境配置文件
├── .env.example            # 环境配置示例
├── .gitignore              # Git 忽略文件
├── requirements.txt        # 项目依赖
└── README.py               # 项目说明文档

---

教学实践详情
============

实践 1: 基础 LLM API 调用 (practice01/llm_client.py)
---------------------------------------------------
功能用途:
    - 演示如何通过原生 Python http.client 模块调用大语言模型(LLM) API
    - 展示如何从 .env 文件加载环境配置（使用 dotenv 库）
    - 演示 HTTP/HTTPS POST 请求的构建和发送
    - 实现与 LLM 的简单对话交互

实现的技术点:
    - os.getenv() - 读取系统环境变量
    - dotenv.load_dotenv() - 加载 .env 配置文件
    - http.client.HTTPConnection / HTTPSConnection - 建立 HTTP 连接
    - json.dumps() - 序列化 Python 对象为 JSON 字符串
    - urllib.parse.urlparse() - 解析 URL
    - API 调用格式（OpenAI 兼容的 /v1/chat/completions 接口）

教学目标:
    - 理解客户端如何与 LLM API 服务进行通信
    - 掌握 HTTP 请求的基本原理和构造方法
    - 学习环境变量管理敏感配置信息
    - 了解 JSON 数据格式在 API 通信中的应用

运行命令:
    python practice01/llm_client.py

---

实践 2: 终端聊天界面 (practice02/chat_interface.py)
--------------------------------------------------
功能用途:
    - 实现交互式终端聊天界面
    - 支持流式输出（实时显示 AI 回复）
    - 自动维护聊天历史记录
    - 支持按 Ctrl+C 退出程序

实现的技术点:
    - 流式响应处理（Streaming Response）
    - 聊天历史上下文管理
    - 异常处理（KeyboardInterrupt）
    - 实时输出和用户输入处理
    - 模块化函数设计

教学目标:
    - 学习如何处理流式 API 响应
    - 理解对话上下文管理的重要性
    - 掌握终端界面的用户交互设计
    - 学习异常处理和程序控制流

运行命令:
    python practice02/chat_interface.py

---

实践 2: 工具调用系统 (practice02/tool_calling.py)
--------------------------------------------------
功能用途:
    - 实现基于 LLM 的工具调用系统
    - 提供 5 个文件操作工具：列出文件、重命名文件、删除文件、创建文件、读取文件
    - 支持通过自然语言指令调用工具
    - 自动处理工具调用和结果处理

实现的技术点:
    - OpenAI 兼容的工具调用格式
    - 函数参数解析和执行
    - 文件系统操作（os 模块）
    - 工具调用流程管理
    - 多轮对话上下文处理

教学目标:
    - 理解 LLM 工具调用的工作原理
    - 学习如何设计和实现工具调用系统
    - 掌握文件系统操作的基本方法
    - 了解如何将工具能力集成到 LLM 应用中

运行命令:
    python practice02/tool_calling.py

---

基础文件
========

1. test.py
----------
功能用途:
    - 最基础的 Python 程序，用于验证开发环境和运行环境是否正常
    - 作为最简单的代码模板，用于测试文件创建和执行流程

实现的技术点:
    - print() 函数的基本使用

教学目标:
    - 确认 Python 解释器配置正确
    - 验证代码文件能够正常执行
    - 作为入门级测试文件

运行命令:
    python test.py

---

配置文件
========

1. .env
-------
用途说明:
    - 存储 API 相关的敏感配置信息
    - 包含以下配置项：
      - BASE_URL：API 服务器地址
      - MODEL_NAME：模型名称
      - API_TOKEN：访问令牌

注意事项:
    - 该文件包含敏感信息，不应提交到版本控制系统
    - 项目已配置 .gitignore 忽略此文件

2. requirements.txt
-------------------
项目依赖:
    - python-dotenv：用于加载 .env 配置文件

安装依赖:
    pip install -r requirements.txt

---

项目运行说明
============
1. 确保已安装 Python 3.x 环境
2. 安装项目依赖：pip install -r requirements.txt
3. 配置 .env 文件，填入真实的 API 地址、模型名称和访问令牌
4. 运行相应的实践文件：
   - 实践 1：python practice01/llm_client.py
   - 实践 2（聊天界面）：python practice02/chat_interface.py
   - 实践 2（工具调用）：python practice02/tool_calling.py
   - 基础测试：python test.py

---

未来规划
========
- practice03/：实现更复杂的功能，如多轮对话管理
- practice04/：添加错误处理和重试机制
- practice05/：实现文件上传和多模态交互

每个实践目录都将包含完整的代码和教学说明，逐步提升难度和功能复杂度。
"""

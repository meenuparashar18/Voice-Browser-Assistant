# 🎙️ Voice Browser Assistant

> Streamlit-based voice-powered browser automation assistant built with **MCP workflows**, **Playwright MCP**, and a **local LLM backend**.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![MCP](https://img.shields.io/badge/MCP-Workflow-orange)
![Playwright](https://img.shields.io/badge/Playwright-Automation-green)
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-purple)

---

## 🌍 Overview

**Voice Browser Assistant** is an AI-powered browser automation assistant that lets users interact with the web using **voice or text commands**.

It combines:
- a **Streamlit interface** for interaction
- **speech recognition** for voice input
- an **MCP-powered workflow** for task orchestration
- **Playwright MCP** for browser actions
- a **local OpenAI-compatible LLM endpoint** (like Ollama) for reasoning and responses

This project is designed for experimenting with **voice-driven browser automation workflows**, where an assistant can understand a request, process it through an LLM, and execute browser-based actions.

---

## ✨ Features

### 🎤 Voice Interaction
Accepts voice input using speech recognition for a more natural user experience.

### 🌐 Browser Automation
Uses **Playwright MCP** to perform browser-based tasks and interactions.

### 🤖 MCP Workflow Integration
Built on an MCP-style workflow setup for handling LLM-powered task execution.

### 💬 Streamlit Interface
Provides an interactive and easy-to-use frontend through Streamlit.

### 🧠 Local LLM Support
Configured to work with an **OpenAI-compatible local API endpoint** such as **Ollama**.

### ⚙️ Config-Driven Setup
Uses a YAML configuration file for MCP server setup, logging, and model configuration.

---

## 🚀 How It Works

1. User enters a **voice or text command**
2. The **Streamlit app** captures the input
3. The request is passed to the **MCP workflow**
4. The configured **LLM** processes the task
5. **Playwright MCP** executes browser-related actions
6. The result is returned and displayed in the UI

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **SpeechRecognition**
- **MCP Agent Framework**
- **Playwright MCP**
- **YAML Configuration**
- **Ollama / OpenAI-compatible local API**
- **Asyncio**

---

## 📁 Project Structure

```bash
Voice-Browser-Assistant/
│
├── main.py                    # Main Streamlit application
├── requirements.txt           # Python dependencies
├── mcp_agent.config.yaml      # MCP + logging + model configuration
├── .gitignore                 # Ignored local/private files
└── README.md                  # Project documentation

```
```bash

Ignored / local-only files

These are intentionally not included in the repository:

mcp_agent.secrets.yaml
.playwright-mcp/
.env
logs/
.venv/ / venv/
__pycache__/

```

---
## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/meenuparashar18/Voice-Browser-Assistant.git
cd Voice-Browser-Assistant
```
---

 ### 2. Create and Activate a Virtual Environment
On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```
---
```bash
On macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

1) Install Python Dependencies
pip install -r requirements.txt

1) Make Sure Node.js and npm Are Installed

This project uses Playwright MCP via npx, so Node.js must be installed.

Check versions:

node -v
npm -v

If these commands don’t work, install Node.js first.

5) Set Up Your Local LLM Backend

This project is configured to use an OpenAI-compatible local endpoint, for example:

openai:
  base_url: "http://localhost:11434/v1"
  default_model: "llama3.2"

That means you should have a local model server running, such as Ollama.

Example:

Install Ollama
Pull the required model
Make sure the endpoint is available at:
http://localhost:11434/v1

6) Configure MCP Settings
The project uses mcp_agent.config.yaml for runtime configuration.

Example config:

execution_engine: asyncio

logger:
  transports: [console, file]
  level: debug
  progress_display: true
  path_settings:
    path_pattern: "logs/mcp-agent-{unique_id}.jsonl"
    unique_id: "timestamp"
    timestamp_format: "%Y%m%d_%H%M%S"

mcp:
  servers:
    playwright:
      command: "npx"
      args: ["@playwright/mcp@latest"]

openai:
  base_url: "http://localhost:11434/v1"
  default_model: "llama3.2"

If your setup requires private secrets, store them separately in:

mcp_agent.secrets.yaml

or

.env

and do not push them to GitHub.

▶️ Run Application

Start the Streamlit app:

streamlit run main.py

Once the app starts, open the local Streamlit URL shown in the terminal (usually http://localhost:8501).



Workflow
Voice/text input is captured
The MCP workflow interprets the task
The LLM decides the next action
Playwright MCP handles browser-side execution
The result is shown back in the Streamlit UI
Output
Voice-assisted browser interaction
AI-guided browser task execution
Interactive workflow experimentation using local LLMs + MCP
📈 Future Improvements
Add support for more browser actions and tools
Improve multi-step task planning and execution
Add memory / chat history support
Improve UI/UX for smoother interaction
Add better error handling and status feedback
Support more LLM providers / remote endpoints
Add deployment support for a hosted demo version

🧠 Learning Outcome
This project helped in exploring:

voice-enabled AI application development
browser automation with MCP workflows
Streamlit-based interactive app development
integrating local LLM endpoints with Python apps
configuration and secret management for GitHub projects
combining voice, browser automation, and agent workflows in one project
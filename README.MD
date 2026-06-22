# Voice Browser Assistant 🎙️🌐

**Voice Browser Assistant** is a Streamlit-based AI browser assistant that combines **voice interaction**, **browser automation**, and **MCP-powered agent workflows**.  
It allows users to interact with the browser using **natural language or voice commands** and execute tasks through an intelligent browser workflow.

The project is designed as an experimental AI assistant that connects a **voice interface**, an **LLM workflow**, and a **browser automation layer** to create a more interactive browsing experience.

---

## ✨ Features

- 🎤 **Voice-enabled interaction** using speech recognition
- 🌐 **Browser automation** through MCP tools
- 🤖 **LLM-powered workflow** for browser-based tasks
- 💬 **Streamlit interface** for interactive usage
- ⚙️ **YAML-based configuration** for MCP setup
- 🧠 Supports an **OpenAI-compatible local LLM endpoint** (e.g. Ollama)
- 🔍 Can be extended for:
  - browser navigation
  - web task automation
  - information extraction
  - conversational browsing workflows

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit**
- **SpeechRecognition**
- **MCP Agent Framework**
- **Playwright MCP**
- **LLM-based workflow orchestration**
- **YAML configuration**
- **Ollama / OpenAI-compatible local API**

---

## 📂 Project Structure

```bash
Voice-Browser-Assistant/
│── main.py
│── requirements.txt
│── .gitignore
│── mcp_agent.config.yaml
│── README.md


🚀 Installation & Setup
1) Clone the repository
git clone https://github.com/meenuparashar18/Voice-Browser-Assistant.git
cd Voice-Browser-Assistant
2) Create a virtual environment (recommended)
On Windows
python -m venv venv
venv\Scripts\activate


On macOS / Linux
python3 -m venv venv
source venv/bin/activate

3) Install Python dependencies
pip install -r requirements.txt

4) Install / set up Node.js
This project uses Playwright MCP through npx, so Node.js and npm should be installed on your system.
Check installation:
node -v
npm -v
If these commands don’t work, install Node.js from the official website before running the project.

5) Set up your local LLM endpoint

This project is configured to use an OpenAI-compatible local API endpoint:

openai:
  base_url: "http://localhost:11434/v1"
  default_model: "llama3.2"

This means you need a compatible local model server running — for example Ollama.

Example:
Install Ollama
Pull the model you want to use
Make sure the local endpoint is available at:
http://localhost:11434/v1

▶️ Run the Project

After setup is complete, start the Streamlit app:

streamlit run main.py



# CodeHelper using CodeLlama-7B

A **coding assistant** built with **CodeLlama-7B**,**Langchain** and **Gradio**.  
This app allows you to ask coding-related questions and get helpful answers in a conversational interface.

---

## 🚀 Features

- Chat with **CodeHelper**, your AI coding assistant.
- Supports multiple programming languages:
  - Python, JavaScript, Java, C++, HTML/CSS, SQL, Linux commands, and more.
- Clean and interactive **Gradio** interface.
- Maintains **conversation history** for follow-up questions.
- Easy to deploy locally.

---

## 🛠️ Installation

1. Install Ollama:
Download and install Ollama from https://ollama.com .

2. Pull the CodeLlama-7B model:
```bash
ollama pull codellama:7b
```
3. Clone the repository:
```bash
git clone https://github.com/sush-sp777/CodeHelper-using-codellama-7b.git
cd CodeHelper-using-codellama-7b
```
4. Create a virtual environment and activate it:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
source venv/bin/activate
```
5. Install required Python packages:
```bash
pip install gradio langchain requests
```
6. Run the Gradio app:
```bash
python app.py
```
---
## ⚡ Usage

- Type your coding question in the input box.
- Click Submit.
- The assistant will respond in the output box.
- Follow-up questions are maintained in conversation history.


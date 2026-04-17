# TheOgBoat 🚤

> The Original AI Chatbot — powered by Groq, LangChain, and Streamlit.
> Fast, free, and runs the most powerful open-source LLMs in the cloud.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![LangChain](https://img.shields.io/badge/LangChain-powered-purple)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## What is TheOgBoat?

**TheOgBoat** is the original, no-nonsense AI chatbot that sails through your questions with speed and precision. Built with cutting-edge tools — Groq's blazing-fast inference, LangChain's powerful prompt chaining, and Streamlit's clean UI — TheOgBoat delivers smart answers without any cloud setup or GPU required.

---

## Features

- ⚡ **Blazing Fast** — powered by Groq's ultra-fast LLM inference
- 🧠 **Multiple Models** — switch between LLaMA 4, LLaMA 3.3, Qwen3, and more
- 🎛️ **Full Control** — adjust temperature and max tokens from the sidebar
- 💬 **Chat History** — full conversation memory within each session
- 🔒 **Private & Secure** — API keys stored safely, never exposed in code
- 📊 **LangSmith Tracking** — monitor and trace every prompt

---

## Demo

```
User: What is the theory of relativity?
TheOgBoat: The theory of relativity, developed by Albert Einstein...
```

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- A free [Groq API key](https://console.groq.com)
- A free [LangSmith API key](https://smith.langchain.com) *(optional)*

### 2. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/TheOgBoat.git
cd TheOgBoat
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langsmith_api_key_here
```

### 5. Run the app
```bash
streamlit run app.py
```

---

## Project Structure

```
TheOgBoat/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .env                # API keys (never commit this)
├── .gitignore          # Ignores .env and venv
└── README.md
```

---

## Available Models

| Model | Best For |
|-------|---------|
| `llama-3.3-70b-versatile` | Best overall performance |
| `llama-3.1-8b-instant` | Fast & lightweight responses |
| `meta-llama/llama-4-scout-17b-16e-instruct` | Latest Llama 4 capabilities |
| `qwen/qwen3-32b` | Strong reasoning & logic |
| `openai/gpt-oss-120b` | Most powerful responses |

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key for LLM inference |
| `LANGCHAIN_API_KEY` | Your LangSmith key for prompt tracking |

---

## Deploying on Streamlit Cloud

1. Push your code to GitHub *(without `.env`)*
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repo
4. Go to **Advanced settings → Secrets** and add:
```toml
GROQ_API_KEY = "your_groq_api_key_here"
LANGCHAIN_API_KEY = "your_langsmith_api_key_here"
```
5. Click **Deploy** 🚀

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Groq](https://groq.com) | Ultra-fast LLM inference |
| [LangChain](https://langchain.com) | Prompt chaining & LLM abstraction |
| [Streamlit](https://streamlit.io) | Web UI |
| [LangSmith](https://smith.langchain.com) | Prompt tracking & observability |
| [python-dotenv](https://pypi.org/project/python-dotenv/) | Environment variable management |

---

## Contributing

Pull requests are welcome! Feel free to open an issue for bugs or feature requests.

---

## License

MIT — feel free to use, modify, and share.

---

<p align="center">Built with ❤️ by samarthx4216 — TheOgBoat ⛵</p>

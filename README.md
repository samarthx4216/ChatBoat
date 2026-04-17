# ChatBoat

> A local AI chatbot powered by Ollama, LangChain, and Streamlit.
> Run open-source LLMs privately — no cloud API costs required.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![LangChain](https://img.shields.io/badge/LangChain-powered-purple)
![Ollama](https://img.shields.io/badge/Ollama-local%20LLM-green)

---

## Features

- Chat with local LLMs (e.g. `gemma:2b`, `llama3`, `mistral`)
- Adjust temperature and max tokens from the sidebar
- LangSmith integration for prompt tracking and observability
- Clean Streamlit UI — no frontend knowledge needed

---

## Getting Started

### 1. Prerequisites
- [Ollama](https://ollama.com) installed and running locally
- Python 3.10+

### 2. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/ChatBoat.git
cd ChatBoat
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root directory:
```
LANGCHAIN_API_KEY=your_langsmith_api_key_here
```

### 5. Pull an Ollama model
```bash
ollama pull gemma:2b
```

### 6. Run the app
```bash
streamlit run app.py
```

---

## Project Structure

```
ChatBoat/
├── app.py              # Main Streamlit app
├── requirements.txt    # Python dependencies
├── .env                # API keys (never commit this)
├── .gitignore
└── README.md
```

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `LANGCHAIN_API_KEY` | Your LangSmith API key for tracing |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Ollama](https://ollama.com) | Run LLMs locally |
| [LangChain](https://langchain.com) | Prompt chaining & LLM abstraction |
| [Streamlit](https://streamlit.io) | Web UI |
| [LangSmith](https://smith.langchain.com) | Prompt tracking & observability |

---

## License

MIT — feel free to use, modify, and share.

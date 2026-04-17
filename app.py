from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

## Langsmith Tracking
os.environ['LANGCHAIN_API_KEY'] = os.getenv("LANGCHAIN_API_KEY", "")
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ["LANGCHAIN_PROJECT"] = "ChatBoat"

## Prompt Template
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please response to the queries"),
    ("user", "Question:{question}")
])

def generate_response(question, engine, temperature, max_tokens):
    llm = ChatGroq(
        model=engine,
        temperature=temperature,
        max_tokens=max_tokens,
        api_key=os.getenv("GROQ_API_KEY")
    )
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer

## Page config
st.set_page_config(page_title="ChatBoat", page_icon="🤖")

## Sidebar
st.sidebar.title("⚙️ Settings")

engine = st.sidebar.selectbox("Select Groq Model", [
    "llama-3.3-70b-versatile",                     # Best overall
    "llama-3.1-8b-instant",                         # Fast & lightweight
    "meta-llama/llama-4-scout-17b-16e-instruct",    # Latest Llama 4
    "qwen/qwen3-32b",                               # Strong reasoning
    "openai/gpt-oss-120b",                          # Most powerful
])

temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=1024, value=256)

st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ using LangChain + Groq + Streamlit")

## Main Interface
st.title("🤖 TheOgBoat")
st.write("Go ahead and ask any question")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

## Display chat history
for chat in st.session_state.chat_history:
    with st.chat_message(chat["role"]):
        st.write(chat["content"])

## Input
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = generate_response(user_input, engine, temperature, max_tokens)
            st.write(response)

    st.session_state.chat_history.append({"role": "assistant", "content": response})
else:
    if not st.session_state.chat_history:
        st.info("Please provide user input")
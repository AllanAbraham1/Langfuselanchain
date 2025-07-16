import os
from dotenv import load_dotenv
import streamlit as st
from langchain_ollama import ChatOllama
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langfuse import Langfuse, observe

# Load environment variables
load_dotenv()

# Initialize Langfuse client
langfuse = Langfuse()
trace_url = None

# Fetch prompt from Langfuse prompt hub
def get_langchain_prompt_template(prompt_name: str, label: str = "production"):
    prompt_client = langfuse.get_prompt(name=prompt_name, label=label)
    prompt_text = prompt_client.prompt
    return PromptTemplate(template=prompt_text, input_variables=["input"])

# Chatbot function with Langfuse tracing
@observe(name="chatbot_interaction")
def get_response(user_input: str, trace=None) -> str:
    global trace_url

    # Log user/session info to Langfuse trace (aka "session")
    if trace:
        trace.update_trace(user_id="user-123")  # Set user
        trace.add_metadata("input_type", "chat")  # Add metadata

    # Get prompt from Langfuse prompt hub
    prompt = get_langchain_prompt_template("Helpassistant")

    # Use Langchain with Ollama
    llm = ChatOllama(model="llama3.1", temperature=0.7)
    chain = LLMChain(llm=llm, prompt=prompt)

    # Run the LLM
    response = chain.invoke({"input": user_input})

    # Log evaluation score and metadata to the same Langfuse session
    if trace:
        trace.add_metric("response_quality", 0.9)  # Example metric
        trace.add_metadata("session_start", True)
        trace_url = trace.url  # Save URL for Streamlit link

    return response["text"]

# Streamlit UI
st.set_page_config(page_title="Langfuse Chatbot", page_icon="🤖")
st.title("🤖 Langfuse Chatbot with Prompt Management")

user_input = st.text_input("You:", "")

if user_input:
    result = get_response(user_input)
    st.markdown("**🤖 Bot:** " + result)

    if trace_url:
        st.markdown(f"[🧪 View Trace in Langfuse]({trace_url})", unsafe_allow_html=True)



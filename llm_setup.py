from langchain_ollama import OllamaLLM
from config import Config

def initialize_llm():
    return OllamaLLM(
        model=Config.OLLAMA_MODEL,
        temperature=0.7,
        top_p=0.9,
    )
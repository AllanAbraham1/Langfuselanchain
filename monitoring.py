from langfuse import Langfuse
from typing import Optional
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class LangfuseMonitor:
    def __init__(self):
        self.client = Langfuse(
            public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
            secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
            host=os.getenv("LANGFUSE_HOST", "https://cloud.langfuse.com")
        )
        if self.client is None:
            print("Langfuse client initialization failed. Check your .env keys.")
            raise RuntimeError(
                "Langfuse client not initialized. Check your .env keys.")
        print("LangfuseMonitor client initialized successfully")

    def update_trace(self, name: Optional[str] = None, user_id: Optional[str] = None, input_data: Optional[dict] = None):
        try:
            # In 3.1.3, trace management is handled by the callback handler
            print(
                f"Trace update attempted with name: {name}, but manual tracing not supported in 3.1.3")
            return None
        except Exception as e:
            print(f"Failed to update trace: {e}")
            return None


def observe_with_langfuse(monitor: LangfuseMonitor, trace_name="Langfuse Trace"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator triggered for function: {func.__name__}")
            try:
                result = func(*args, **kwargs)
                print(
                    "Function executed successfully, score logging relies on callback handler")
                return result
            except Exception as e:
                print(f"Function failed with error: {e}")
                raise
        return wrapper
    return decorator

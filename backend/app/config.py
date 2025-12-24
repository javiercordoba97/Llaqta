import os
from dotenv import load_dotenv

load_dotenv()
print("DEBUG KEY:", os.getenv("HUGGINGFACE_API_KEY"))

class Settings:
    OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY", "")
    DEFAULT_LLM_MODEL = os.getenv("DEFAULT_LLM_MODEL", "mistralai/Mistral-7B-Instruct-v0.2")

settings = Settings()
print(">>> LLM_SERVICE (OPENROUTER) CARGADO <<<")

import requests
from app.config import settings
import json

def generate_llm_response(user_message: str):
    if not settings.OPENROUTER_API_KEY:
        return {"error": "No se encontró la clave de API de OpenRouter"}

    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {settings.OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": settings.DEFAULT_LLM_MODEL,
        "messages": [
            {"role": "user", "content": user_message}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code != 200:
        return {
            "error": "Error al conectar con OpenRouter",
            "details": response.text
        }

    data = response.json()

    try:
        return data["choices"][0]["message"]["content"]
    except:
        return {"error": "No se pudo interpretar la respuesta del modelo."}
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

    # --- SYSTEM PROMPT MEJORADO ---
    system_prompt = """
    Sos LlaqtaBot, asistente oficial de Llaqta, una tienda argentina de ropa de campo.
    Tu estilo es amable, claro y directo.
    No inventes productos ni información.
    Si no sabés algo, pedí más detalles.
    Respondé SIEMPRE en texto plano, sin JSON, sin listas numeradas a menos que el usuario lo pida.
    Usá un tono natural, argentino y profesional.
    """

    payload = {
        "model": settings.DEFAULT_LLM_MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
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
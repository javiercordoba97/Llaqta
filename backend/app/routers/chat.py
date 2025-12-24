from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_service import generate_llm_response
from app.services.nutrition_service import get_nutrition_data
import json

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/")
async def chat(request: ChatRequest):
    user_message = request.message.strip().lower()

    # --- RESPUESTA CORTA PARA SALUDOS ---
    saludos = ["hola", "buenas", "hey", "holaa", "ola"]
    if user_message in saludos:
        return {
            "type": "general",
            "data": "Hola, ¿cómo estás?"
        }

    # --- PROMPT MEJORADO ---
    llm_prompt = f"""
    Tu tarea es analizar el mensaje del usuario y devolver SOLO un JSON válido.

    Reglas estrictas:
    1. Si el alimento está mal escrito, corregilo. Ejemplos:
       - "mansana" → "manzana"
       - "paltta" → "palta"
       - "bananna" → "banana"
    2. Si el usuario escribe un alimento con errores, asumí la intención correcta.
    3. Si el mensaje no menciona un alimento, poné "food": null.
    4. NO inventes productos comerciales ni marcas.
    5. NO mezcles idiomas. Respondé siempre en español.
    6. NO devuelvas texto fuera del JSON.
    7. El campo "question" debe contener la versión corregida del mensaje del usuario.

    Formato obligatorio:

    {{
        "intent": "nutrition" o "general",
        "food": "nombre del alimento o null",
        "question": "pregunta original corregida"
    }}

    Mensaje del usuario: "{user_message}"
    """

    llm_raw = generate_llm_response(llm_prompt)

    try:
        parsed = json.loads(llm_raw)
    except Exception as e:
        return {
            "type": "general",
            "data": "Disculpa, no entendí lo que quisiste decir. ¿Podrías explicármelo de otra forma?"
        }

    intent = parsed.get("intent")
    food = parsed.get("food")

    # --- NUTRICIÓN ---
    if intent == "nutrition" and food:
        nutrition = get_nutrition_data(food)
        if nutrition:
            return {
                "type": "nutrition",
                "food": food,
                "data": nutrition
            }
        else:
            return {
                "type": "nutrition",
                "food": food,
                "error": f"No se encontró información para '{food}'"
            }

    # --- GENERAL (respuesta corta, sin modelo) ---
    return {
        "type": "general",
        "data": "Disculpa, no entendí lo que quisiste decir. ¿Podrías explicármelo de otra forma?"
    }
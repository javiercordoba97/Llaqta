def detect_intent(message: str) -> str:
    """
    Detecta si el usuario está preguntando por información nutricional.
    Si encuentra palabras clave relacionadas con alimentos o nutrición,
    devuelve 'nutrition'. Si no, devuelve 'general'.
    """

    message = message.lower()

    # Palabras clave que indican intención nutricional
    nutrition_keywords = [
        "calorías", "calorias", "proteínas", "proteinas", "carbohidratos",
        "azúcar", "azucar", "grasas", "fibra", "sodio",
        "nutrición", "nutricion", "nutrientes",
        "cuántas calorías tiene", "cuanta calorias tiene",
        "información nutricional", "informacion nutricional",
        "macros", "macro", "nutrimental"
    ]

    # Si el mensaje contiene alguna palabra clave → nutrición
    if any(keyword in message for keyword in nutrition_keywords):
        return "nutrition"

    # Si no coincide con nada → respuesta general del LLM
    return "general"
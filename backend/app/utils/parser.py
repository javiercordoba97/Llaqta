def extract_food_name(message: str) -> str:
    """
    Extrae un posible nombre de alimento desde el mensaje del usuario.
    Esta versión es simple: devuelve el mensaje tal cual.
    Más adelante podemos mejorarla con NLP o regex.
    """
    return message.strip()
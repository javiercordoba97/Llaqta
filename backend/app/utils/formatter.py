def format_nutrition_response(data: dict) -> str:
    """
    Formatea la información nutricional en un texto legible.
    """

    if "error" in data:
        return data["error"]

    nombre = data.get("nombre", "Desconocido")
    calorias = data.get("calorias", "N/A")
    proteinas = data.get("proteinas", "N/A")
    carbohidratos = data.get("carbohidratos", "N/A")
    azucares = data.get("azucares", "N/A")
    grasas = data.get("grasas", "N/A")
    fibra = data.get("fibra", "N/A")
    sodio = data.get("sodio", "N/A")

    return (
        f"Información nutricional por 100g de **{nombre}**:\n"
        f"- Calorías: {calorias}\n"
        f"- Proteínas: {proteinas}g\n"
        f"- Carbohidratos: {carbohidratos}g\n"
        f"- Azúcares: {azucares}g\n"
        f"- Grasas: {grasas}g\n"
        f"- Fibra: {fibra}g\n"
        f"- Sodio: {sodio}g\n"
    )
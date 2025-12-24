import requests
from app.config import settings

def get_nutrition_data(food_name: str):
    """
    Busca un alimento en Open Food Facts y devuelve
    información nutricional básica.
    """

    # Endpoint de búsqueda
    search_url = "https://world.openfoodfacts.org/cgi/search.pl"

    params = {
        "search_terms": food_name,
        "search_simple": 1,
        "action": "process",
        "json": 1,
    }

    response = requests.get(search_url, params=params)

    if response.status_code != 200:
        return {"error": "Error al conectar con Open Food Facts"}

    data = response.json()

    # Si no hay productos encontrados
    if "products" not in data or len(data["products"]) == 0:
        return {"error": f"No se encontró información para '{food_name}'"}

    products = data["products"]

    # --- 1. Detectar si el usuario pidió un alimento simple ---
    palabras = food_name.split()
    alimento_simple = len(palabras) == 1  # Ej: "manzana", "palta", "banana"

    # --- 2. Si es alimento simple, buscar coincidencias exactas ---
    if alimento_simple:
        for p in products:
            nombre = p.get("product_name", "").lower()

            # Coincidencia exacta o muy cercana
            if nombre == food_name.lower() or food_name.lower() in nombre.split():
                nutriments = p.get("nutriments", {})
                return {
                    "nombre": p.get("product_name", "Desconocido"),
                    "calorias": nutriments.get("energy-kcal_100g"),
                    "proteinas": nutriments.get("proteins_100g"),
                    "carbohidratos": nutriments.get("carbohydrates_100g"),
                    "azucares": nutriments.get("sugars_100g"),
                    "grasas": nutriments.get("fat_100g"),
                    "fibra": nutriments.get("fiber_100g"),
                    "sodio": nutriments.get("sodium_100g"),
                }

        # Si no encontramos coincidencia exacta, devolvemos el primero
        # (pero avisamos que puede no ser el alimento puro)
        p = products[0]
        nutriments = p.get("nutriments", {})
        return {
            "nombre": p.get("product_name", "Desconocido"),
            "advertencia": "No se encontró el alimento exacto, mostrando el producto más cercano.",
            "calorias": nutriments.get("energy-kcal_100g"),
            "proteinas": nutriments.get("proteins_100g"),
            "carbohidratos": nutriments.get("carbohydrates_100g"),
            "azucares": nutriments.get("sugars_100g"),
            "grasas": nutriments.get("fat_100g"),
            "fibra": nutriments.get("fiber_100g"),
            "sodio": nutriments.get("sodium_100g"),
        }

    # --- 3. Si es un producto compuesto, devolvemos el primero ---
    product = products[0]
    nutriments = product.get("nutriments", {})

    return {
        "nombre": product.get("product_name", "Desconocido"),
        "calorias": nutriments.get("energy-kcal_100g"),
        "proteinas": nutriments.get("proteins_100g"),
        "carbohidratos": nutriments.get("carbohydrates_100g"),
        "azucares": nutriments.get("sugars_100g"),
        "grasas": nutriments.get("fat_100g"),
        "fibra": nutriments.get("fiber_100g"),
        "sodio": nutriments.get("sodium_100g"),
    }
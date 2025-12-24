from fastapi import APIRouter
from app.services.nutrition_service import get_nutrition_data

router = APIRouter()

@router.get("/search")
def search_food(food_name: str):
    """
    Endpoint para buscar información nutricional de un alimento
    usando Open Food Facts.
    """
    result = get_nutrition_data(food_name)
    return result
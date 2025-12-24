from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import chat, nutrition

app = FastAPI(
    title="NutriBot API",
    description="Backend de NutriBot: chatbot nutricional con LLM + Open Food Facts",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(chat.router, prefix="/chat", tags=["Chat"])
app.include_router(nutrition.router, prefix="/nutrition", tags=["Nutrition"])

@app.get("/")
def root():
    return {"message": "NutriBot API funcionando correctamente"}
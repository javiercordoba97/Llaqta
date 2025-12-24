from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    type: str   # "nutrition" o "llm"
    data: dict  # contenido de la respuesta

class LLMRequest(BaseModel):
    prompt: str

class LLMResponse(BaseModel):
    response: str
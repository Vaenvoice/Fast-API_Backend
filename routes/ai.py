from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AIRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

class AIResponse(BaseModel):
    response: str
    tokens_used: int

@router.get("/")
async def get_ai_status():
    """Get AI service status"""
    return {"message": "AI service is available", "status": "active"}

@router.post("/generate")
async def generate_ai_response(request: AIRequest):
    """Generate AI response"""
    return AIResponse(
        response=f"AI response to: {request.prompt}",
        tokens_used=request.max_tokens
    )

@router.get("/models")
async def get_available_models():
    """Get available AI models"""
    return {"message": "Available models", "models": ["gpt-3.5", "gpt-4", "claude"]}
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter()

class AIRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

class AIResponse(BaseModel):
    response: str
    tokens_used: int

class AIHighlight(BaseModel):
    label: str
    confidence: float
    x: float
    y: float
    width: float
    height: float

class AIHighlightsResponse(BaseModel):
    image_id: int
    highlights: List[AIHighlight]

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


@router.get("/highlight/{image_id}", response_model=AIHighlightsResponse)
async def get_ai_highlights(image_id: int):
    """Return mock JSON of AI highlights with bounding boxes and labels"""
    
    # Static mock data
    mock_highlights = [
        AIHighlight(
            label="vehicle",
            confidence=0.95,
            x=120.5,
            y=80.3,
            width=200.0,
            height=150.0
        ),
        AIHighlight(
            label="person",
            confidence=0.87,
            x=350.2,
            y=200.1,
            width=80.0,
            height=180.0
        ),
        AIHighlight(
            label="building",
            confidence=0.92,
            x=50.0,
            y=30.0,
            width=300.0,
            height=250.0
        ),
        AIHighlight(
            label="tree",
            confidence=0.78,
            x=500.0,
            y=100.0,
            width=120.0,
            height=200.0
        )
    ]
    
    return AIHighlightsResponse(
        image_id=image_id,
        highlights=mock_highlights
    )
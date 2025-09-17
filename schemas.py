from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


# Image schemas
class ImageBase(BaseModel):
    title: str
    mission: str
    date: date
    url: str


class ImageCreate(ImageBase):
    pass


class ImageResponse(ImageBase):
    id: int
    
    class Config:
        from_attributes = True


# Annotation schemas
class AnnotationBase(BaseModel):
    image_id: int
    user_id: str
    label: str
    x: float
    y: float
    width: float
    height: float


class AnnotationCreate(AnnotationBase):
    pass


class AnnotationResponse(AnnotationBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
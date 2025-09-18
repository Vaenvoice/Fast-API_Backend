from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List

# ---------------------------
# Image Schemas
# ---------------------------

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
        orm_mode = True  # ✅ This allows Pydantic to read from SQLAlchemy objects


# ---------------------------
# Annotation Schemas
# ---------------------------

class AnnotationBase(BaseModel):
    image_id: int
    user_id: int
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
        orm_mode = True

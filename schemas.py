from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional, List, Dict, Any

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
        orm_mode = True


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


# ---------------------------
# Visit Schemas
# ---------------------------

class VisitResponse(BaseModel):
    count: int

    class Config:
        orm_mode = True


# ---------------------------
# Event Schemas
# ---------------------------

class EventIn(BaseModel):
    event_type: str
    payload: Optional[Dict[str, Any]] = None
    session_id: Optional[str] = None

class EventResponse(BaseModel):
    id: int
    event_type: str
    payload: Optional[Dict[str, Any]]
    session_id: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True


from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Annotation
from schemas import AnnotationCreate, AnnotationResponse

router = APIRouter()


@router.post("/", response_model=AnnotationResponse)
async def create_annotation(annotation: AnnotationCreate, db: Session = Depends(get_db)):
    """Create a new annotation"""
    db_annotation = Annotation(**annotation.model_dump())
    db.add(db_annotation)
    db.commit()
    db.refresh(db_annotation)
    return db_annotation


@router.get("/{image_id}", response_model=List[AnnotationResponse])
async def get_annotations_by_image(image_id: int, db: Session = Depends(get_db)):
    """Get all annotations for a given image"""
    annotations = db.query(Annotation).filter(Annotation.image_id == image_id).all()
    return annotations
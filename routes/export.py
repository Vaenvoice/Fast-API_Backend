from fastapi import APIRouter, Depends, HTTPException, Query
from fastapi.responses import PlainTextResponse
from sqlalchemy.orm import Session
from typing import List, Literal
from database import get_db
from models import Annotation
from schemas import AnnotationResponse
import csv
import io
import json

router = APIRouter()


@router.get("/{image_id}")
async def export_annotations(
    image_id: int,
    format: Literal["csv", "json"] = Query("json", description="Export format: csv or json"),
    db: Session = Depends(get_db)
):
    """Return annotations for an image in the requested format"""
    
    # Query annotations for the specific image
    annotations = db.query(Annotation).filter(Annotation.image_id == image_id).all()
    
    if format == "json":
        # Return JSON format using Pydantic serialization
        annotation_responses = [AnnotationResponse.model_validate(annotation) for annotation in annotations]
        return annotation_responses
    
    elif format == "csv":
        # Return CSV format
        if not annotations:
            return PlainTextResponse("id,image_id,user_id,label,x,y,width,height,created_at\n", media_type="text/csv")
        
        # Create CSV output
        output = io.StringIO()
        writer = csv.writer(output)
        
        # Write header
        writer.writerow(["id", "image_id", "user_id", "label", "x", "y", "width", "height", "created_at"])
        
        # Write data rows
        for annotation in annotations:
            writer.writerow([
                annotation.id,
                annotation.image_id,
                annotation.user_id,
                annotation.label,
                annotation.x,
                annotation.y,
                annotation.width,
                annotation.height,
                annotation.created_at.isoformat()
            ])
        
        csv_content = output.getvalue()
        output.close()
        
        return PlainTextResponse(csv_content, media_type="text/csv")
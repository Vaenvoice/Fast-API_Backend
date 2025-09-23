from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Visit
from schemas import VisitResponse

router = APIRouter(prefix="/visits", tags=["Visits"])


@router.get("/", response_model=VisitResponse)
def get_visit_count(db: Session = Depends(get_db)):
    visit = db.query(Visit).first()
    if not visit:
        visit = Visit(count=0)
        db.add(visit)
        db.commit()
        db.refresh(visit)
    return {"count": visit.count}


@router.post("/", response_model=VisitResponse)
def increment_visit_count(db: Session = Depends(get_db)):
    visit = db.query(Visit).first()
    if not visit:
        visit = Visit(count=1)
        db.add(visit)
    else:
        visit.count += 1
    db.commit()
    db.refresh(visit)
    return {"count": visit.count}

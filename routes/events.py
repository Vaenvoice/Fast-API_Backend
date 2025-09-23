from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Event
from schemas import EventIn, EventResponse

router = APIRouter(prefix="/events", tags=["Events"])


@router.post("/", response_model=EventResponse)
def log_event(event: EventIn, db: Session = Depends(get_db)):
    new_event = Event(
        event_type=event.event_type,
        payload=event.payload,
        session_id=event.session_id,
    )
    db.add(new_event)
    db.commit()
    db.refresh(new_event)
    return new_event


@router.get("/", response_model=list[EventResponse])
def get_all_events(db: Session = Depends(get_db)):
    return db.query(Event).order_by(Event.created_at.desc()).all()

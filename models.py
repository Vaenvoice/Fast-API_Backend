from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey, JSON, func
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)

    # relationships
    annotations = relationship("Annotation", back_populates="user")


class Image(Base):
    __tablename__ = "images"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    mission = Column(String, nullable=False)
    date = Column(Date, nullable=True)
    url = Column(String, nullable=False)

    # Relationship to annotations
    annotations = relationship("Annotation", back_populates="image")


class Annotation(Base):
    __tablename__ = "annotations"

    id = Column(Integer, primary_key=True, index=True)
    image_id = Column(Integer, ForeignKey("images.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="annotations")
    label = Column(String, nullable=False)
    x = Column(Float, nullable=False)
    y = Column(Float, nullable=False)
    width = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    # Relationship to image
    image = relationship("Image", back_populates="annotations")


# ---------------------------
# New Models for Counter + Analytics
# ---------------------------

class Visit(Base):
    __tablename__ = "visits"

    id = Column(Integer, primary_key=True, index=True)
    count = Column(Integer, nullable=False, default=0)
    # We'll keep only one row (id=1) and increment this


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, index=True)  # e.g. "zoom", "pan", "search"
    payload = Column(JSON, nullable=True)    # store event details as JSON
    session_id = Column(String, nullable=True)
    created_at = Column(DateTime, server_default=func.now())

from sqlalchemy import Column, Integer, String, Float, Date, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class User(Base):
    __tablename__= "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)

    #relationships
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
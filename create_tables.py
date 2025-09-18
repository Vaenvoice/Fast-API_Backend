# create_tables.py
from database import Base, engine
# import models so SQLAlchemy knows about them
import models

Base.metadata.create_all(bind=engine)
print("Tables created (or already exist).") 

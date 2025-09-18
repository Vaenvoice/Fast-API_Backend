from datetime import datetime, date
from database import SessionLocal
import models

# Start DB session
db = SessionLocal()

# ------------------------
# 1. Seed a dummy user
# ------------------------
user = models.User(username="astro_user")
db.add(user)
db.commit()
db.refresh(user)

# ------------------------
# 2. Seed an image
# ------------------------
image = models.Image(
    title="Lunar Surface",
    mission="Apollo 11",
    date=date(1969, 7, 20),  # optional, since you made date nullable
    url="https://example.com/tiles/lunar_dzi"
)
db.add(image)
db.commit()
db.refresh(image)

# ------------------------
# 3. Seed an annotation
# ------------------------
annotation = models.Annotation(
    image_id=image.id,
    user_id=user.id,   # ✅ linked to user
    label="Crater-1",
    x=100.0,
    y=150.0,
    width=50.0,
    height=60.0,
    created_at=datetime.utcnow()
)
db.add(annotation)
db.commit()

print("✅ Seed data inserted successfully!")
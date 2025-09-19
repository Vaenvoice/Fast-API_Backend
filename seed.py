from datetime import datetime, date
from database import SessionLocal
import models

def seed():
    db = SessionLocal()

    # ------------------------
    # 1. Seed a dummy user
    # ------------------------
    user = db.query(models.User).filter_by(username="astro_user").first()
    if not user:
        user = models.User(username="astro_user")
        db.add(user)
        db.commit()
        db.refresh(user)

    # ------------------------
    # 2. Seed an image
    # ------------------------
    image = db.query(models.Image).filter_by(title="Lunar Surface").first()
    if not image:
        image = models.Image(
            title="Lunar Surface",
            mission="Apollo 11",
            date=date(1969, 7, 20),
            url="/static/tiles/lunar_surface"  # ✅ update later to your Render URL
        )
        db.add(image)
        db.commit()
        db.refresh(image)

    # ------------------------
    # 3. Seed an annotation
    # ------------------------
    annotation = db.query(models.Annotation).filter_by(label="Crater-1").first()
    if not annotation:
        annotation = models.Annotation(
            image_id=image.id,
            user_id=user.id,
            label="Crater-1",
            x=100.0,
            y=150.0,
            width=50.0,
            height=60.0,
            created_at=datetime.utcnow()
        )
        db.add(annotation)
        db.commit()

    db.close()
    print("✅ Seed data inserted successfully!")

if __name__ == "__main__":
    seed()

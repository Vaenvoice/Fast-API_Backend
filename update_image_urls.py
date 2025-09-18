from sqlalchemy.orm import Session
from database import get_db
from models import Image  # make sure your model name is correct

# Replace this with your actual Render URL where the tiles are hosted
RENDER_BASE_URL = "https://fast-api-backend1.onrender.com/static/tiles"

def update_image_urls():
    db: Session
    db = next(get_db())  # get a database session

    images = db.query(Image).all()
    for img in images:
        # assuming the DZI folder name matches img.title
        new_url = f"{RENDER_BASE_URL}/{img.title.replace(' ', '_')}"
        print(f"Updating Image ID {img.id}: {img.url} -> {new_url}")
        img.url = new_url

    db.commit()
    print("All image URLs updated successfully!")

if __name__ == "__main__":
    update_image_urls()

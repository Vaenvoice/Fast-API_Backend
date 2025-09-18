from PIL import Image
import os
import math

SOURCE_DIR = "images_source"
TILES_DIR = "static/tiles"
TILE_SIZE = 256

def save_tile(img, x, y, level_dir):
    tile_path = os.path.join(level_dir, f"{x}_{y}.png")
    img.save(tile_path)

def create_dzi(image_path, output_dir):
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    img = Image.open(image_path)
    width, height = img.size

    # Create folder for this image
    image_tiles_dir = os.path.join(output_dir, image_name)
    os.makedirs(image_tiles_dir, exist_ok=True)

    # Calculate levels
    max_dim = max(width, height)
    max_level = math.ceil(math.log2(max_dim))

    for level in range(max_level, -1, -1):
        scale = 2 ** (max_level - level)
        level_width = math.ceil(width / scale)
        level_height = math.ceil(height / scale)
        level_img = img.resize((level_width, level_height), Image.LANCZOS)

        # Folder for this level
        level_dir = os.path.join(image_tiles_dir, str(level))
        os.makedirs(level_dir, exist_ok=True)

        # Generate tiles
        x_tiles = math.ceil(level_width / TILE_SIZE)
        y_tiles = math.ceil(level_height / TILE_SIZE)

        for x in range(x_tiles):
            for y in range(y_tiles):
                left = x * TILE_SIZE
                upper = y * TILE_SIZE
                right = min(left + TILE_SIZE, level_width)
                lower = min(upper + TILE_SIZE, level_height)
                tile = level_img.crop((left, upper, right, lower))
                save_tile(tile, x, y, level_dir)

        print(f"Created level {level} tiles for {image_name}")

# Process all images
for filename in os.listdir(SOURCE_DIR):
    if filename.lower().endswith((".png", ".jpg", ".jpeg")):
        create_dzi(os.path.join(SOURCE_DIR, filename), TILES_DIR)

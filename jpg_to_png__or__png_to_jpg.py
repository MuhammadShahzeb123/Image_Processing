from PIL import Image
import os

Files = os.listdir()

images = [item for item in Files if item.endswith('.jpg') or item.endswith('jpeg') or item.endswith('.webp')]

height, width = 500, 500

for image in images:
    with Image.open(image) as img:
        img.resize((width, height)).save(f"{image[:-5]}.png" if image.endswith('.jpeg') else f"{image[:-4]}.png")
        img.close()
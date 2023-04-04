from PIL import Image
import os
import sys

images = [f for f in os.listdir() if f.endswith('jpg')]

count = 0
for image in images:
    count = str(count)
    with Image.open(image) as img:
            img.convert('RGB').save(f"{count}.jpg".replace('.png', '.jpg'), 'JPEG')
    os.remove(image)
    count = int(count)
    count += 1
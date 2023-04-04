import os
from PIL import Image

# Get a list of all image files in the directory
dir = os.listdir()
image_files = [f for f in dir if f.endswith('.jpg')]
# Convert the landscape images to portrait orientation
for image_file in image_files:
    img = Image.open(image_file)
    if img.width > img.height:
        img = img.rotate(270, expand=True)
        img.save(image_file)

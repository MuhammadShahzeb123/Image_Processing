# import os
# import img2pdf
# import natsort as n

# dr = os.listdir()
# files = [f for f in dr if f.endswith('.jpg')]
# files_sorted = n.natsorted(dr)

# # print(files)
# with open('output.pdf', 'wb') as f:
#         f.write(img2pdf.convert(files_sorted, rotation=img2pdf.Rotation.ifvalid))

import os
import img2pdf

# Get a list of all image files in the directory
dir = os.listdir()
image_files = [f for f in dir if f.endswith('.jpg') or f.endswith('.png')]

# Convert the images to a PDF
try:
    with open('output.pdf', 'wb') as f:
        f.write(img2pdf.convert(image_files, rotation=img2pdf.Rotation.ifvalid))
except img2pdf.ImageOpenError as e:
    print(f"Error: {e}")

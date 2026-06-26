import numpy as np
from PIL import Image

img = Image.open("./img.jpg")
print("PIL image size:", img.size)

img_array = np.array(img)
print("Numpy array size:", img_array.shape)

print("Pixel at (0,0):", img_array[0,0])
import numpy as np
from PIL import Image

img = Image.open("./img.jpg")
print("PIL image size:", img.size)

img_array = np.array(img)
print("Numpy array size:", img_array.shape)

print("Pixel at (0,0):", img_array[0,0])

R = img_array[:, :, 0]
G = img_array[:, :, 1]
B = img_array[:, :, 2]

grey_manual = 0.299 * R + 0.587 * G + 0.114 * B
grey_manual = grey_manual.astype(np.uint8)

print("grey_manual:", grey_manual.shape)

img_grey_manual = Image.fromarray(grey_manual)
img_grey_manual.save("img_grey.jpg")

img_grey_pil = img.convert("L")
grey_pil_array = np.array(img_grey_pil)

print("grey_pil shape:", grey_pil_array.shape)
print("max difference:", np.max(np.abs(grey_manual.astype(int) - grey_pil_array.astype(int))))

rotated_90 = np.rot90(grey_manual)
print("rotated_shape:", rotated_90.shape)

img_rotated = Image.fromarray(rotated_90)
img_rotated.save("img_rotated.jpg")

def blur(image):
    h, w = image.shape
    kernel = np.ones((3, 3)) / 9

    output = np.zeros((h, w))

    for i in range(1, h - 1):
        for j in range(1, w - 1):
            region = image[i-1:i+2, j-1:j+2]
            output[i, j] = np.sum(region * kernel)

    return output.astype(np.uint8)

blurred = blur(grey_manual)
img_blurred = Image.fromarray(blurred)
img_blurred.save("img_blurred.jpg")



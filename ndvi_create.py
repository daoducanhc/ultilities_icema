import cv2
from PIL import Image
import numpy as np

nir = Image.open("nir.png").convert("L")
nir = np.asarray(nir, dtype=np.uint16)
red = Image.open("red.png").convert("L")
red = np.asarray(red, dtype=np.uint16)

a = (nir - red).astype(np.int16)
b = (nir + red).astype(np.uint16)

output = np.divide(a, b, where=b != 0)
output = cv2.normalize(output, output, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
output = np.rint(output)
output = output.astype(np.uint8)
image = Image.fromarray(output)
image.save("ndvi.png")

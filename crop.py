from PIL import Image
import cv2

path = 'dataset/3m/'

mask = cv2.imread(path + 'mask/0.png')
red = cv2.imread(path + 'red/0.png')
nir = cv2.imread(path + 'nir/0.png')
ndvi = cv2.imread(path + 'ndvi/0.png')

y = 0
x = 1600

nir = nir[y:y+2048, x:x+2048]
mask = mask[y:y+2048, x:x+2048]
red = red[y:y+2048, x:x+2048]
ndvi = ndvi[y:y+2048, x:x+2048]

cv2.imwrite("nir.png", nir)
cv2.imwrite("red.png", red)
cv2.imwrite("ndvi.png", ndvi)
cv2.imwrite("mask.png", mask)

# cv2.imshow("img", cv2.resize(nir, (600,600), interpolation = cv2.INTER_AREA))
# cv2.waitKey(0)
import cv2
import numpy as np

calib = cv2.imread("calib_nir.png")

ratio = 127.5 / np.mean(calib)

calib = cv2.convertScaleAbs(calib, alpha=ratio)

np.mean(calib)

img = cv2.imread("nir.png")
img = cv2.convertScaleAbs(img, alpha=ratio)

cv2.imshow("IMG", cv2.resize(img, (700,700), interpolation = cv2.INTER_AREA))
cv2.imwrite("nir.png", img)
cv2.waitKey(0)

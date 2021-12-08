import cv2

img = cv2.imread('8m.jpg')

(nir, _, red) = cv2.split(img)

# cv2.imshow("red", cv2.resize(red, (700,700), interpolation = cv2.INTER_AREA))
# cv2.imshow("nir", cv2.resize(nir, (700,700), interpolation = cv2.INTER_AREA))

cv2.imwrite("red.png", red)
cv2.imwrite("nir.png", nir)

# cv2.waitKey(0)

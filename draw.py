import cv2

path = "8m_mask.png"

mask = cv2.imread(path)

mask = cv2.circle(mask,(1700,1900), 40, (0,0,255), -1)
mask = cv2.circle(mask,(1900,1900), 40, (0,255,0), -1)

cv2.imwrite(path, mask)

# cv2.imshow("IMG", cv2.resize(mask, (700,700), interpolation = cv2.INTER_AREA))
# cv2.waitKey(0)

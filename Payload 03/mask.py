import cv2
import numpy as np

img = cv2.imread("source.jpg")

mask = np.zeros(img.shape[:2], dtype="uint8")
cv2.circle(mask, (750, 750), 80, 255, -1)
masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imwrite('masked.jpg', masked)

import cv2
import numpy as np

im = cv2.imread("filled.jpg")

kernel1 = np.ones((5, 5), np.uint8)
kernel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

erosion = cv2.erode(im, kernel1)
dialation = cv2.dilate(im, kernel1)

opening = cv2.morphologyEx(im, cv2.MORPH_OPEN, kernel2)
closing = cv2.morphologyEx(im, cv2.MORPH_CLOSE, kernel2)

cv2.imwrite("erosion.jpg", erosion)
cv2.imwrite("dialation.jpg", dialation)

cv2.imwrite("opening.jpg", opening)
cv2.imwrite("closing.jpg", closing)
cv2.waitKey(0)

import cv2
import numpy as np

im = cv2.imread('source.jpg')
im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(im, (5, 5), 0)
cv2.imwrite("target.jpg", im)

(T, threshInv) = cv2.threshold(blurred, 155, 255, cv2.THRESH_BINARY_INV)
cv2.imwrite("simple thresholding.jpg", cv2.bitwise_and(im, im, mask=threshInv))

thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 15, 3)
cv2.imwrite("adaptive thresholding.jpg", thresh)

thresh = im.copy()
thresh[thresh > T] = 255
thresh[thresh < 255] = 0
thresh = cv2.bitwise_not(thresh)
cv2.imwrite("Otsu's method.jpg", thresh)

cv2.waitKey(0)
import numpy as np
import cv2

im = cv2.imread("source.jpg")

im = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

cv2.imwrite("Original.jpg", im)

lap = cv2.Laplacian(im, cv2.CV_64F)

lap = np.uint8(np.absolute(lap))

cv2.imwrite("Laplacian.jpg", lap)

sobelX = cv2.Sobel(im, cv2.CV_64F, 1, 0)
sobelY = cv2.Sobel(im, cv2.CV_64F, 0, 1)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv2.bitwise_or(sobelX, sobelY)

cv2.imwrite("Sobel X.jpg", sobelX)
cv2.imwrite("Sobel Y.jpg", sobelY)
cv2.imwrite("Sobel Combined.jpg", sobelCombined)

cv2.waitKey(0)

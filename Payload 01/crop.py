from __future__ import print_function
import argparse
import cv2
ap = argparse.ArgumentParser()
args = vars(ap.parse_args())

image = cv2.imread('TC.jpg')
cv2.imshow("Original", image)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))
corner = image[100:400, 400:800]
cv2.imshow("Corner", corner)
cv2.imwrite('C.jpg', corner)

image[100:400, 400:800] = (0, 0, 255)

cv2.imshow("Updated", image)
cv2.imwrite('LO.jpg', image)
cv2.waitKey(0)

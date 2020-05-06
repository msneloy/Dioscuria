import cv2
import numpy as np
im = cv2.imread("source.jpg")
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (11, 11), 0)
edged = cv2.Canny(blurred, 30, 150)
(cnts, _) = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL,
                             cv2.CHAIN_APPROX_SIMPLE)
print("{} contours detected in this image".format(len(cnts)))
contours = im.copy()
cv2.drawContours(contours, cnts, -1, (0, 0, 255), 2)
cv2.imwrite("Contures.jpg", contours)
h, w, c = im.shape
print('image width:  ', w)
print('image height: ', h)
print('image channel:', c)
cv2.waitKey(0)

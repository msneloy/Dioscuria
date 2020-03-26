import numpy as np
import cv2
im = cv2.imread('source.jpg')
noise = np.hstack([
cv2.blur(im, (9, 9)),
cv2.medianBlur(im, 9),
cv2.bilateralFilter(im, 9, 99, 99),
cv2.GaussianBlur(im, (9, 9), 0)])
cv2.imwrite('noise.jpg', noise)
cv2.waitKey(0)
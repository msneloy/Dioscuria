import cv2
import numpy as np

img = cv2.imread('canvas.jpg')

M = np.float32([[1, 0, -100], [0, 1, -100]])
shift = cv2.warpAffine(img, M, (400, 400))

cv2.imwrite('shift.jpg', shift)
cv2.waitKey(0)

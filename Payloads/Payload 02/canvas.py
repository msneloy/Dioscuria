import cv2
import numpy as np

canvas = cv2.imread('canvas.jpg')

R = (0, 0, 255)
G = (0, 255, 0)
B = (255, 0, 0)
W = (255, 255, 255)

cv2.line(canvas, (335, 65), (65, 335), R, 3)
cv2.rectangle(canvas, (400, 0), (0, 400), R, 5)
cv2.circle(canvas, (200, 200), 190, R, 3)

cv2.imwrite('drawing.jpg', canvas)
cv2.waitKey(0)

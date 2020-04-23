import cv2
import numpy as np
im = cv2.imread("source.jpg")
drawing = np.zeros(im.shape[:], dtype=np.uint8)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150)
drawing = np.zeros(im.shape[:], dtype=np.uint8)

circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20, param2=30)
circles = np.int0(np.around(circles))

for i in circles[0, :]:
    cv2.circle(drawing, (i[0], i[1]), i[2], (0, 255, 0), 2)
    cv2.circle(drawing, (i[0], i[1]), 2, (0, 0, 255), 3)

lines = cv2.HoughLines(edges, 0.8, np.pi / 180, 90)

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a * rho
    y0 = b * rho
    x1 = int(x0 + 1000 * (-b))
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

cv2.line(drawing, (x1, y1), (x2, y2), (0, 0, 255))
cv2.imwrite("Gray.jpg", gray)
cv2.imwrite("Canny.jpg", edges)
cv2.imwrite("drawing.jpg", drawing)
cv2.waitKey(0)

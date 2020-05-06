import cv2

img = cv2.imread("source.jpg")

(h, w) = img.shape[:2]
center = (w / 2, h / 2)

M = cv2.getRotationMatrix2D(center, 60, 0.4)
rotated = cv2.warpAffine(img, M, (w, h))

cv2.imwrite('rotated.jpg', rotated)

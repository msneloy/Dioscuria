import cv2
import numpy as np

im = cv2.imread("source.jpg")

im_floodfill = im.copy()

h, w = im.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

cv2.floodFill(im_floodfill, mask, (200, 200), (255, 255, 255),
              (50, 20, 50), (50, 50, 30), cv2.FLOODFILL_FIXED_RANGE)

cv2.floodFill(im_floodfill, mask, (900, 600), (255, 255, 255),
              (50, 20, 50), (50, 50, 30), cv2.FLOODFILL_FIXED_RANGE)

cv2.floodFill(im_floodfill, mask, (100, 1000), (255, 255, 255),
              (50, 20, 50), (50, 50, 30), cv2.FLOODFILL_FIXED_RANGE)

cv2.floodFill(im_floodfill, mask, (1000, 100), (255, 255, 255),
              (50, 20, 50), (50, 50, 30), cv2.FLOODFILL_FIXED_RANGE)

cv2.imwrite("filled.jpg", im_floodfill)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("source.jpg")

mask = np.zeros(img.shape[:2], np.uint8)

cv2.circle(mask, (350, 100), 100, 255, -1)
cv2.circle(mask, (100, 100), 100, 255, -1)

masked_img = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("masked_img", masked_img)

for i, col in enumerate(['b', 'g', 'r']):
    hist_mask = cv2.calcHist([img], [i], mask, [256], [0, 256])
    plt.plot(hist_mask, color=col)

plt.show()

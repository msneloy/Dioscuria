import cv2
import matplotlib.pyplot as plt

img = cv2.imread('source.jpg')

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

g_hist = cv2.calcHist([gray_img], [0], None, [256], [0, 256])
plt.plot(g_hist, color="K")

for i, col in enumerate(['b', 'g', 'r']):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)

plt.show()

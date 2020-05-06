import cv2
cv2.namedWindow("Color Image")
im = cv2.imread('TC.jpg')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
cv2.imwrite('GS.jpg', gray)
cv2.imshow("Color Image", im)
cv2.waitKey(0)
cv2.destroyAllWindows()
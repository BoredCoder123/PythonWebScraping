import cv2
import numpy as np

image = cv2.imread('redHat.jpg')

# hsv = hue sat value
# hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# lower_red = np.array([150, 150, 50])
# upper_red = np.array([180, 255, 150])
#
# mask = cv2.inRange(hsv, lower_red, upper_red)
# res = cv2.bitwise_and(image, image, mask=mask)

# kernel = np.ones((15, 15), np.float32)/225
# smooth = cv2.filter2D(res, -1, kernel)
# blur = cv2.GaussianBlur(res, (15, 15), 0)
# median = cv2.medianBlur(res, 15)
# bilateral = cv2.bilateralFilter(res, 15, 75, 75)

# kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(mask, kernel, iterations=1)
# dilations = cv2.dilate(mask, kernel, iterations=1)
#
# opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

laplacion = cv2.Laplacian(image, cv2.CV_64F)
sobelx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
edges = cv2.Canny(image, 125, 175)

cv2.imshow('image', image)
# cv2.imshow('res', res)
# cv2.imshow('mask', mask)
# cv2.imshow('smooth', smooth)
# cv2.imshow('blue', blur)
# cv2.imshow('median', median)
# cv2.imshow('bilateral', bilateral)

# cv2.imshow('erosion', erosion)
# cv2.imshow('dilate', dilations)
# cv2.imshow('opening', opening)
# cv2.imshow('closing', closing)
# BlackHat and Top hat also exists

cv2.imshow('laplacion', laplacion)
cv2.imshow('sobelx', sobelx)
cv2.imshow('sobely', sobely)
cv2.imshow('edges', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()

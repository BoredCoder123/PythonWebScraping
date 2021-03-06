import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

px = img[55, 55]
img[55, 55] = [0, 0, 0]

# Region of image roi

watchFace = img[37:111, 107:194]
img[0:74, 0:87] = watchFace

img[100:150, 100: 150] = [0, 0, 0]
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


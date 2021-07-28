import cv2
import numpy as np

image1 = cv2.imread('i1.png')
image2 = cv2.imread('i2.png')
image3 = cv2.imread('python.png')

# add = image1 + image2
# add = cv2.add(image1, image2)
# weighted = cv2.addWeighted(image1, 0.6, image2, 0.4, 0)

# cv2.imshow('add', weighted)

rows, cols, channels = image3.shape
roi = image1[0: rows, 0: cols]

image2gray = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(image2gray, 220, 255, cv2.THRESH_BINARY_INV)
# cv2.imshow('mask', mask)

mask_inv = cv2.bitwise_not(mask)
image1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
image2_fg = cv2.bitwise_and(image3, image3, mask=mask)

dst = cv2.add(image1_bg, image2_fg)
image1[0:rows, 0:cols] = dst
cv2.imshow('res', image1)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont


def createWatermarkFromImage(image, watermark, opacity, x, y):
    opacity = opacity / 100
    rows, cols, channels = watermark.shape
    roi = image[y: rows+y, x: cols+x]

    image2gray = cv2.cvtColor(watermark, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(image2gray, 220, 255, cv2.THRESH_BINARY_INV)
    # cv2.imshow('mask', mask)

    mask_inv = cv2.bitwise_not(mask)
    image1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
    image2_fg = cv2.bitwise_and(watermark, watermark, mask=mask)

    dst = cv2.add(image1_bg, image2_fg)
    image[y:rows+y, x:cols+x] = dst
    # cv2.addWeighted(dst, opacity / 100, image, 1 - opacity / 100, 0, image)
    return image


def createWatermarkFromText(image, watermark, opacity, x, y):
    overlay = image.copy()
    output = image.copy()
    cv2.putText(overlay, watermark, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 255), 3)
    cv2.addWeighted(overlay, opacity / 100, output, 1 - opacity / 100, 0, output)
    return output

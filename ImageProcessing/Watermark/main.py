import cv2
import createWatermark
from PIL import Image, ImageFont, ImageDraw

image = cv2.imread("images/image.jpg")
watermark = 'Ankit Kathait'
opacity = 30
x = 818
y = 247

# result = createWatermark.createWatermarkFromText(image, watermark, opacity, x, y)
# cv2.imshow('fromImage', result)
# cv2.waitKey(0)

watermark = cv2.imread('images/watermark.png')
result = createWatermark.createWatermarkFromImage(image, watermark, opacity, x, y)
cv2.imshow('fromImage', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

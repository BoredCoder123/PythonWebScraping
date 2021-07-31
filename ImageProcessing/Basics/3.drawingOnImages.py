import numpy as np
import cv2

img = cv2.imread('watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (0, 0), (150, 150), (0, 255, 255), 3)    # cv2 works in BGR mode
cv2.rectangle(img, (15, 25), (200, 150), (255, 0, 255), 5)
cv2.circle(img, (70, 70), 40, (0, 0, 255), 5)  # -1 fills the circle

pts = np.array([[10, 10], [60, 30], [70, 60], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
cv2.polylines(img, [pts], True, (0, 0, 255), 3)   # 3rd True means connect the first and the last point

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'Open CV', (150, 150), font, 1, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

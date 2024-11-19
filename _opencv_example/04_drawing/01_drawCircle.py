import cv2
import numpy as np

image_path = "Images/cat.jpg"
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)
img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
img_gray_color = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

h, w, c = img_gray_color.shape

center = (w//2, h//2)

cv2.circle(img_gray_color, center, 150, (0, 0, 255), 5)

cv2.imshow('cat with red circle', img_gray_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
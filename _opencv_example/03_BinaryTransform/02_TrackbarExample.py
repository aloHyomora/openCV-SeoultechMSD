import cv2
import numpy as np

# Trackbar : OpenCV에서 GUI 요소로 사용됨. 동적 매개변수를 슬라이더를 통해 조정 가능

image_path = "Images/boat.jpg"
img = cv2.imread(image_path)
cv2.namedWindow("Trackbar Example")

# 트랙바 콜백 함수
def change_brightness(value):
    # 슬라이더 값으로 이미지를 밝게 만듬
    brightness = int(value)
    updated_img = np.clip(img + brightness, 0, 255).astype(np.uint8)
    cv2.imshow('Trackbar Example', updated_img)
    
cv2.createTrackbar('Brightness', 'Trackbar Example', 0, 255, change_brightness)

cv2.imshow('Trackbar Example', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
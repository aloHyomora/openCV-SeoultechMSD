import cv2

# 1. 왜 gray로 바꿨다가 다시 BGR로 바꾸나요?
# 그레이스케일 변환: OTSU 이진화를 적용하려면 입력 이미지가 그레이스케일이어야 합니다.
# BGR 변환: 텍스트를 추가하려면 이미지가 BGR 형식이어야 하므로, 이진화 후 다시 BGR로 변환합니다.
# 2. OTSU의 사용 목적은 무엇인가요?
# OTSU는 이미지를 자동으로 이진화하는 방법입니다.
# 사용자가 직접 임계값(Threshold)을 지정하지 않아도, 픽셀 값의 분포를 분석해 최적의 임계값을 계산합니다.
# 결과적으로 객체와 배경을 명확히 분리합니다.

image_path = "Images/snake.jpg"
img_color = cv2.imread(image_path, cv2.IMREAD_COLOR)
img_color = cv2.resize(img_color, (0,0), interpolation=cv2.INTER_CUBIC, fx=0.5,fy=0.5)

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
_, img_bin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_OTSU)

img_bin_color = cv2.cvtColor(img_bin, cv2.COLOR_GRAY2BGR)
h,w,c = img_bin_color.shape

center = (w//2,h//2)
cv2.putText(img_bin_color, "Snake", center, cv2.FONT_HERSHEY_SIMPLEX, 2.0, (255,0,0), 5)
cv2.imshow('Snake', img_bin_color)
cv2.waitKey(0)
cv2.destroyAllWindows()
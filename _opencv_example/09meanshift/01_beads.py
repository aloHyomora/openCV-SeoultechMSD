# 여러 개의 비드의 수를 세는 프로그램을 허프 변환을 이용하여 작성한다. 
# 비드의 중심에 녹색 사각형 외곽에 청색 원을 그리고 좌측 상단에 개수를 출력한다.

# imread —> medianBlur —> cvtColor —> HoughCircles

import cv2
import numpy as np

# 이미지를 읽어오기
img = cv2.imread('C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/beads1.png')

# 이미지를 3x3 커널로 미디언 블러링 처리 (잡음 제거)
img_blur = cv2.medianBlur(img, 3)

# 블러 처리된 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

# 허프 변환을 사용하여 원 검출 수행
# cv2.HoughCircles(입력 이미지, 검출 방법, 해상도 비율, 최소 거리, 다른 매개변수들...)
circles = cv2.HoughCircles(
    gray,
    cv2.HOUGH_GRADIENT,  # 허프 그래디언트 방법 사용
    1,                  # 축소 비율 (1은 동일 해상도 유지)
    8,                  # 원 중심 간 최소 거리
    param1=220,         # 엣지 검출을 위한 Canny 상위 임계값
    param2=22,          # 원 검출을 위한 내부 임계값
    minRadius=5,        # 검출할 최소 반지름
    maxRadius=30        # 검출할 최대 반지름
)

# 원이 검출된 경우
if circles is not None:
    # 원 정보를 반올림하여 정수로 변환 (x, y, 반지름)
    circles = np.round(circles[0, :]).astype(np.int16)

    # 검출된 각 원에 대해
    for (x, y, r) in circles:
        # 원을 이미지에 그림 (파란색, 두께 2)
        cv2.circle(img, (x, y), r, (255, 0, 0), 2)
        # 원 중심에 작은 사각형으로 표시 (녹색, 두께 -1은 채우기)
        cv2.rectangle(img, (x - 2, y - 2), (x + 2, y + 2), (0, 255, 0), -1)

# 검출된 원의 개수를 표시할 문자열 생성
display = f'{len(circles)} beads'

# 이미지에 문자열 추가 (좌측 상단, 빨간색 글자, 크기 0.8)
font, LT = cv2.FONT_HERSHEY_SIMPLEX, cv2.LINE_AA
cv2.putText(img, display, (20, 20), font, 0.8, (0, 0, 255), 2)

# 결과 이미지 출력
cv2.imshow('detected circles', img)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

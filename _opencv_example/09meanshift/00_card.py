import cv2
import numpy as np

# 이미지를 읽어오기
img = cv2.imread('C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/tag1.png')

# 이미지를 그레이스케일로 변환 (허프 변환을 위한 전처리)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Canny 에지 검출을 사용하여 엣지 이미지 생성
edges = cv2.Canny(gray, 80, 200, apertureSize=3)  # 최소 임계값 80, 최대 임계값 200
cv2.imshow('edges', edges)  # 에지 결과 출력

# 허프 변환으로 직선 검출
lines = cv2.HoughLines(edges, 1, np.pi / 180, 160)  # (픽셀 거리 해상도=1, 각도 해상도=1°, 임계값=160)
lines = lines.reshape((-1, 2))  # 결과를 2D 배열로 변환 (rho와 theta)

# 검출된 모든 직선을 순회하며 그리기
for rho, theta in lines:
    # 직선의 극좌표(rho, theta)를 직교좌표로 변환
    a, b = np.cos(theta), np.sin(theta)  # cos(theta)와 sin(theta) 계산
    x0, y0 = a * rho, b * rho  # 직선의 중심 좌표 (rho * cos(theta), rho * sin(theta))

    # 직선의 시작점(x1, y1)과 끝점(x2, y2) 계산
    x1 = int(x0 + 1000 * (-b))  # 직선을 충분히 확장 (1000 픽셀)
    y1 = int(y0 + 1000 * (a))
    x2 = int(x0 - 1000 * (-b))
    y2 = int(y0 - 1000 * (a))

    # 원래 이미지에 직선 그리기
    cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 1)  # 녹색 선, 두께 1

# 검출된 직선 결과 이미지 출력
cv2.imshow('detected lines', img)

# 키 입력 대기 및 모든 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

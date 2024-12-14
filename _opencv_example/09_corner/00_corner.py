import cv2
import numpy as np

# 이미지를 읽어와 복사본을 만듦
img = cv2.imread('C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/shapes.png')
img2 = np.copy(img)

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# cv2.goodFeaturesToTrack: Shi-Tomasi 코너 검출 알고리즘으로 코너를 탐색하고, 해당 코너를 이미지에 시각적으로 표시.
# maxCorners=500: 최대 검출할 코너 수
# qualityLevel=0.04: 코너로 판단할 최소 품질 수준
# minDistance=10: 코너 간 최소 거리
corners = cv2.goodFeaturesToTrack(gray, 500, 0.04, 10)

# 코너를 빨간색 점으로 표시
col = (0, 0, 255)
for con in corners:
    center = [int(e) for e in con[0]]  # 코너의 중심 좌표
    cv2.circle(img, center, 3, col, -1)  # 중심 좌표에 반지름 3인 빨간 점 그리기

# 코너 검출 결과 출력
cv2.imshow('KLT', img)

# cv2.cornerHarris: Harris 코너 검출 알고리즘으로 코너 응답값을 계산하고, 응답값이 높은 영역을 강조.
gray = np.float32(gray)  # Harris 코너 검출을 위해 데이터 타입을 float32로 변환
dst = cv2.cornerHarris(gray, 2, 3, 0.01)  # 코너 응답값 계산
# blockSize=2: 각 픽셀의 이웃 영역 크기
# ksize=3: Sobel 커널 크기
# k=0.01: Harris 응답 방정식의 감도 계수

# 응답값을 팽창시켜 더 두드러지게 만듦
dst = cv2.dilate(dst, None)

# Harris 응답값이 임계값보다 큰 영역을 빨간색으로 표시
img2[dst > 0.005 * dst.max()] = [0, 0, 255]

# Harris 코너 검출 결과 출력
cv2.imshow('Hrris', img2)

# ESC 키를 누르면 창 닫기
if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
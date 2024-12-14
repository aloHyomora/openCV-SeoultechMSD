import cv2
import numpy as np

# 커널 생성 (5x5 크기의 모든 요소가 1인 배열)
kernel = np.ones((5,5), np.uint8)

# 이미지를 읽어오기
img = cv2.imread('C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/coupling.jpg')

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이진화 수행: 임계값 100을 기준으로 255(흰색) 또는 0(검은색)으로 변환
_, binary = cv2.threshold(gray, 100, 255, 0)

# 열림 연산 수행: 작은 노이즈 제거 및 객체의 외곽선 부드럽게 하기
opening = cv2.morphologyEx(binary, cv2.MORPH_OPEN, kernel)

# 외곽선 찾기: 가장 바깥 외곽선만 검색
contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# 첫 번째 외곽선을 선택
cnt = contours[0]

# 최소 영역 사각형 계산 (기울어진 사각형)
rect = cv2.minAreaRect(cnt)

# 사각형의 각도, 너비, 높이 출력
angle = rect[2]
print(f'width={rect[1][0]}, height={rect[1][1]}, angle={angle}')

# 사각형의 꼭짓점 좌표 계산
pts = cv2.boxPoints(rect).reshape((-1, 1, 2))

# 이미지에 사각형을 그리기
cv2.polylines(img, [np.int32(pts)], True, (0, 0, 255), 2)

# 이미지의 크기 정보 가져오기
rows, cols = img.shape[:2]

# 회전 변환 행렬 생성: 중심점을 기준으로 각도만큼 회전
M = cv2.getRotationMatrix2D((cols//2, rows//2), angle, 1)

# 회전 변환을 적용하여 이미지 회전
rotated = cv2.warpAffine(img, M, (cols, rows))

# 이진화 이미지 출력
cv2.imshow('binary', binary)

# 외곽선이 그려진 이미지 출력
cv2.imshow('bounding box', img)

# 회전된 이미지 출력
cv2.imshow('rotated', rotated)

# 키 입력 대기 후 모든 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

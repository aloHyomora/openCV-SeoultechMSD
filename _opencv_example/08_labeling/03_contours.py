import cv2
import numpy as np

kernel = np.ones((7,7), np.uint8)
img = cv2.imread("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/lego.jpg")
cv2.imshow("Original", img)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray",gray)

# 이진화(Binarization): 밝기가 210 이상인 픽셀을 255(흰색)으로 설정하고, 나머지는 0(검정색)으로 설정
_, bin = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY_INV)
cv2.imshow("Binary", bin)

# 모폴로지 연산(Morphological Operation): 'CLOSE' 연산으로 작은 구멍(0)을 채워 연속된 객체로 만듦
bin_d = cv2.morphologyEx(bin, cv2.MORPH_CLOSE, kernel)

# cv2.connectedComponentsWithStats를 사용하여 연결된 컴포넌트 분석
# cnt: 연결된 컴포넌트의 개수
# labels: 각 픽셀이 속한 컴포넌트의 레이블
# stats: 각 컴포넌트의 통계 정보 (x, y, w, h, area)
# centroids: 각 컴포넌트의 중심점 좌표
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(bin_d)

count = 1  # 컴포넌트 번호를 매기기 위한 변수
for i in range(1, cnt):  # 0번은 배경이므로 제외하고 반복
    x, y, w, h, area = stats[i]  # 현재 컴포넌트의 통계 정보 가져오기 (x, y: 위치, w: 폭, h: 높이, area: 면적)
    if area < 70:  # 면적이 70보다 작으면 작은 노이즈로 간주하고 무시
        continue
    cx, cy = [int(e) for e in centroids[i]]  # 컴포넌트의 중심점 좌표(cx, cy)를 정수로 변환
    # 중심점에 검은색 원 그리기
    cv2.circle(img, (cx, cy), 5, (0, 0, 0), -1)
    # 중심점 근처에 컴포넌트 번호와 면적을 표시
    cv2.putText(img, f'[{count}] : {area}', (cx + 10, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 0)
    count += 1  # 컴포넌트 번호 증가

# 이진화된 이미지에서 윤곽선(Contour) 추출
contours, _ = cv2.findContours(bin_d, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

# 추출한 윤곽선을 원본 이미지에 그리기
for cnt in contours:
    cv2.drawContours(img, [cnt], 0, (0, 0, 255), 2)  # 윤곽선 색: 빨간색 (BGR), 두께: 2

# 모폴로지 연산 결과 이미지 표시
cv2.imshow("Morphing", bin_d)

# 윤곽선을 그린 이미지 표시
cv2.imshow("Contour", img)

# 키 입력 대기 및 모든 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()
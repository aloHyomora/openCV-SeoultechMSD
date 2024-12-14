import cv2

# 원본 이미지를 컬러 모드로 읽음
src = cv2.imread("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/uscoins.png", cv2.IMREAD_COLOR)

# 이미지를 그레이스케일로 변환
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

# 노이즈 제거를 위해 중간값 블러링(Median Blur) 적용
blured = cv2.medianBlur(gray, 15)

# 임계값을 이용해 이진화 수행 (240 이상의 값을 0으로, 나머지는 255로 설정)
ret, binary = cv2.threshold(blured, 240, 255, cv2.THRESH_BINARY_INV)

# 연결된 구성 요소를 분석 (레이블링, 통계 정보, 중심점)
cnt, labels, stats, centroids = cv2.connectedComponentsWithStats(binary)

# 카운터 초기화 (레이블 번호)
count = 1

# 레이블 1부터 시작 (레이블 0은 배경)
for i in range(1, cnt):
    # 레이블 i에 대한 통계 정보 (x, y는 좌상단 좌표, w: 너비, h: 높이, area: 영역 크기)
    (x, y, w, h, area) = stats[i]

    # 작은 영역(면적이 70 미만)은 무시
    if area < 70:
        continue

    # 레이블 i의 중심점(cx, cy)
    cx, cy = centroids[i]
    center = (int(cx), int(cy))

    # 사각형의 좌상단(pt1)과 우하단(pt2) 좌표 계산
    pt1 = (x, y)
    pt2 = (x + w, y + h)

    # 중심을 기준으로 반지름 (w+h)/4의 원을 그림 (주황색)
    cv2.circle(src, center, int((w + h) / 4), (0, 150, 255), 4)

    # 중심점에 작은 원을 그림 (빨간색)
    cv2.circle(src, center, 4, (0, 0, 255), -1)

    # 텍스트로 레이블 번호와 영역 크기(area)를 표시 (파란색)
    cv2.putText(src, f'[{count}]: area={area}', (int(cx - w / 3), int(cy - h / 3)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    # 레이블 카운트 증가
    count += 1

# 변환된 그레이스케일 이미지를 출력
cv2.imshow('Gray', gray)

# 이진화된 이미지를 출력
cv2.imshow('Binary', binary)

# 결과 이미지 출력 (레이블링, 중심점, 원 및 텍스트 포함)
cv2.imshow('Result', src)

# 키 입력 대기 후 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

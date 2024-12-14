import cv2
import numpy as np

# 함수: 이미지를 주어진 크기로 확장하여 색상 및 값을 시각적으로 표시
def genColored(simg, sz):
    # 지정된 크기의 빈 컬러 이미지를 생성 (3채널, 검은색 초기화)
    im = np.zeros((sz[1], sz[0], 3), np.uint8)
    
    # 입력 이미지의 행(row)과 열(column) 크기 추출
    rows, cols = simg.shape[:2]
    
    # 각 셀의 가로 및 세로 크기를 계산
    dc, dr = sz[0] // cols, sz[1] // rows
    
    # 행과 열을 순회하며 각 셀에 대해 처리
    for r in range(rows):
        for c in range(cols):
            # 현재 셀의 시작 및 끝 좌표를 계산
            r0, r1, c0, c1 = dr * r, dr * (r + 1), dc * c, dc * (c + 1)
            
            # 현재 셀의 값 (0 또는 1 등)
            v = simg[r, c]
            
            # 셀의 색상을 `colors` 배열에서 해당 값에 맞는 색으로 채움
            im[r0:r1, c0:c1] = colors[v]
            
            # 값이 0이면 흰색 글자, 0이 아니면 검은색 글자로 표시
            color = (255, 255, 255) if v == 0 else (0, 0, 0)
            
            # 셀 중앙에 값을 텍스트로 그려줌
            cv2.putText(im, f'{v}', (c0 + 40, r0 + 60), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        color, 1, cv2.LINE_AA)
    return im

# 색상 테이블: 각 숫자 값에 매핑되는 색상 정의
colors = [(0, 0, 0), (0, 255, 0), (128, 128, 0), (0, 128, 128), (128, 0, 128), (0, 0, 255), (255, 0, 0)]

# 8x9 크기의 이진 이미지 생성
img = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 1, 0, 0, 0],
                [0, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]], dtype=np.uint8)

# 입력 이미지를 확장하고 표시
big = genColored(img, (900, 800))
cv2.imshow('binary', big)

# 입력 이미지의 모멘트 계산
M = cv2.moments(img)

# 모멘트를 이용해 이미지의 면적과 중심점 계산
area = M['m00']  # 면적 계산, 이미지의 면적(픽셀 값 합계). 비이진 이미지에서는 흰색 픽셀 값의 총합을 나타냅니다.
center = (M['m10'] / area, M['m01'] / area)  # 중심점 계산, 각각 x축과 y축에 대해 계산된 모멘트 값으로, 무게중심을 계산할 때 사용됩니다.

# 면적과 중심점 출력
print(f' area={area} pixels')
print(f' center ={center}')

# 중심점을 시각적으로 표시하기 위해 복사본 생성
marked = genColored(img, (900, 800))

# 중심점 좌표를 정수로 변환 (픽셀 단위)
cx, cy = int(np.round(center[0] * 100)), int(np.round(center[1] * 100))

# 중심점에 원을 그려 시각적으로 표시 (파란색 원)
cv2.circle(marked, (cx, cy), 10, colors[5], 2)

# 중심점이 표시된 이미지 출력
cv2.imshow('center', marked)

# 키 입력 대기 및 창 닫기
cv2.waitKey(0)
cv2.destroyAllWindows()

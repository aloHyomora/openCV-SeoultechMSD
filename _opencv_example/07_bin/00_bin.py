import cv2
import numpy as np

# 선의 색상 정의 (오렌지색)
linecolor = (255, 128, 0)

# 이진 이미지를 큰 이미지로 시각화하는 함수
def genImg(bin, size):
    rows, cols = bin.shape  # 입력 이미지의 행(row)과 열(col) 크기 가져오기
    # 확대된 이미지 크기만큼 검은색(RGB 값 0, 0, 0)으로 초기화
    im = np.zeros((int(rows * size), int(cols * size), 3), np.uint8)
    for r in range(rows):  # 각 행을 반복
        for c in range(cols):  # 각 열을 반복
            r0, r1, c0, c1 = size * r, size * (r + 1), size * c, size * (c + 1)  # 확대된 영역 좌표 계산
            value = bin[r, c]  # 현재 위치의 이진 값(0 또는 1)을 가져옴
            # 픽셀 값(0은 검은색, 1은 흰색)으로 채우기
            im[r0:r1, c0:c1] = (value * 255, value * 255, value * 255)
            # 값에 따라 텍스트 색상 설정 (0이면 흰색, 1이면 검은색)
            color = (255, 255, 255) if value == 0 else (0, 0, 0)
            # 확대된 영역에 픽셀 값을 텍스트로 표시
            cv2.putText(im, f'{value}', (c0 + size // 3 + 5, r0 + size // 2 + 10),  
                        cv2.FONT_HERSHEY_SIMPLEX, size / 75, color, 1, cv2.LINE_AA)
    # 각 행에 대한 선 그리기
    for r in range(rows):
        cv2.line(im, (0, r * size), (cols * size, r * size), linecolor, 1)
    # 각 열에 대한 선 그리기
    for c in range(cols):
        cv2.line(im, (c * size, 0), (c * size, rows * size), linecolor, 1)
    return im  # 생성된 이미지를 반환

# 침식(Erosion) 함수 정의
def erode(bin):
    rows, cols = bin.shape  # 이진 이미지의 행(row)과 열(col) 크기 가져오기
    # 원본 이미지에 패딩(테두리 추가)을 적용
    pading = np.zeros((rows + 2, cols + 2), np.uint8)
    pading[1:rows + 1, 1:cols + 1] = bin  # 원본 이미지를 가운데 삽입
    out = np.zeros((rows, cols), np.uint8)  # 출력 이미지 초기화
    for r in range(rows):  # 각 행 반복
        for c in range(cols):  # 각 열 반복
            # 3x3 커널 안의 모든 값이 1인 경우만 출력 값으로 1 설정
            out[r, c] = 1 if pading[r:r + 3, c:c + 3].all() else 0
    return out  # 침식된 이미지 반환

# 팽창(Dilation) 함수 정의
def dilate(bin):
    rows, cols = bin.shape  # 이진 이미지의 행(row)과 열(col) 크기 가져오기
    pading = np.zeros((rows + 2, cols + 2), np.uint8)  # 원본 이미지에 패딩 추가
    pading[1:rows + 1, 1:cols + 1] = bin  # 원본 이미지를 가운데 삽입
    out = np.zeros((rows, cols), np.uint8)  # 출력 이미지 초기화
    for r in range(rows):  # 각 행 반복
        for c in range(cols):  # 각 열 반복
            # 3x3 커널 안의 값 중 하나라도 1인 경우 출력 값으로 1 설정
            out[r, c] = 1 if pading[r:r + 3, c:c + 3].any() else 0
    return out  # 팽창된 이미지 반환

# 이진 이미지 생성
bin = np.array(
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0],
     [0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    dtype=np.uint8)

# 각종 이미지 처리 적용
bin_e = erode(bin)  # 침식
bin_d = dilate(bin)  # 팽창
bin_o = dilate(bin_e)  # Opening 연산
bin_c = erode(bin_d)  # Closing 연산

# 결과 출력
cv2.imshow("Original", genImg(bin, 50))  # 원본 이미지
#cv2.imshow("Erode", genImg(bin_e, 50))  # 침식
#cv2.imshow("Dilate", genImg(bin_d, 50))  # 팽창
cv2.imshow("Opening", genImg(bin_o, 50))  # Opening: 노이즈가 많은 이미지 → 불필요한 점이나 얇은 돌출부가 사라짐.
cv2.imshow("Closing", genImg(bin_c, 50))  # Closing: 객체 내부에 구멍이 있는 이미지 → 구멍이 메워지고 객체가 연결됨.
cv2.waitKey(0)
cv2.destroyAllWindows()

# kxk 커널을 사용하여 평균 필터인 aveFilter 함수를 만들고 lena.jpg에 적용해본다.
# 단, padding을 사용하고 k는 홀수라 가정한다. 또한 opencv의 filter2D의 결과와 비교해본다.
# 커널은 이미지 처리를 위해 사용하는 작은 행렬(matrix)

import cv2
import  numpy as np

def aveFilter(img, k=3):
    N = k**2 # 커널 크기에 해당하는 픽셀 크기
    half = k//2 # 커널 크기의 반쪽으로, 패딩된 이미지에서 중심 위치를 계산하기 위해 사용됨.
    rows, cols = img.shape[:2]  # 입력 이미지의 세로와 가로 크기를 나타낸다.
    print(rows, cols)
    padded = np.zeros((rows+k-1, cols+k-1),dtype=np.uint8) # 패딩된 이미지를 저장하는 배열로 필터를 이미지 가장자리까지 적용하기 위해 필요하다.
    padded[half:rows+half, half:cols+half] = img
    
    dst = np.zeros_like(img)    # 필터가 적용된 최종 이미지를 저장한다.
    for r in range(rows):
        for c in range(cols):
            val = np.sum(padded[r:r+k,c:c+k])
            dst [r,c] = int(val/N)
    return dst
    
    

img = cv2.imread("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/lena.jpg", cv2.IMREAD_GRAYSCALE)  # 그레이스케일 이미지로 읽기
cv2.imshow("Original Image", img)  # 원본 이미지 출력

fltImg = aveFilter(img, 5) # 5x5 커널  사용해서 평균 필터 적용
cv2.imshow("filter img", fltImg)

cv2.waitKey(0)
cv2.destroyAllWindows()

























# import cv2
# import numpy as np

# def aveFilter(src, k=3):
#     """
#     평균 필터를 적용하는 함수
#     :param src: 입력 이미지 (numpy 배열 형태)
#     :param k: 커널 크기 (홀수여야 함)
#     :return: 평균 필터가 적용된 이미지
#     """
#     N = k ** 2  # 커널 크기에 해당하는 픽셀 개수
#     half = k // 2  # 커널의 반쪽 크기
#     rows, cols = src.shape[:2]  # 입력 이미지의 행과 열

#     print(f"이미지 크기: {rows} x {cols}")

#     # 입력 이미지를 패딩 처리
#     padded = np.zeros((rows + k - 1, cols + k - 1), dtype=np.uint8)  # 패딩된 이미지 초기화
#     padded[half:rows + half, half:cols + half] = src  # 패딩 처리된 이미지에 원본 삽입

#     # 출력 이미지를 원본과 같은 크기로 초기화
#     dst = np.zeros_like(src)

#     # 평균 필터 계산 (슬라이딩 윈도우 방식)
#     for r in range(rows):
#         for c in range(cols):
#             # 커널 영역의 값 합산
#             val = np.sum(padded[r:r + k, c:c + k])
#             # 평균값 계산 후 픽셀에 할당
#             dst[r, c] = int(val / N)

#     return dst

# # lena 이미지를 읽어와 평균 필터 적용
# img = cv2.imread("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/lena.jpg", cv2.IMREAD_GRAYSCALE)  # 그레이스케일 이미지로 읽기
# cv2.imshow("Original Image", img)  # 원본 이미지 출력

# flt = aveFilter(img, 5)  # 커널 크기 5x5로 평균 필터 적용
# cv2.imshow("Filtered Image", flt)  # 필터링된 이미지 출력

# # OpenCV의 filter2D 함수로 동일한 필터링 수행
# kernel = np.ones((5, 5), np.float32) / 25  # 5x5 평균 필터 커널 생성
# opencv_filtered = cv2.filter2D(img, cv2.CV_8U, kernel)
# cv2.imshow("OpenCV Filtered Image", opencv_filtered)  # OpenCV 필터링 결과 출력

# cv2.waitKey(0)
# cv2.destroyAllWindows()

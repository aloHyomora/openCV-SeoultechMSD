import cv2
import numpy as np

img = cv2.imread("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/lena.jpg")
img = cv2.cvtColor(img, 0)

# 감마 보정 이미지의 밝기를 조절하는 비선형 변환이다.
# gamma > 1: 어두운 영역을 더 어둡게, 밝은 영역은 더 밝게
# gamma < 1: 어두운 영역을 더 밝게, 밝은 영역은 더 어둡게

# 감마 보정 테이블 생성
gamma = 1.7
table = np.array([np.power(i/255.0, gamma)*255 for i in range(256)], dtype=np.uint8)
print(table)

# 생성한 감마 보정 테이블을 원본 이미지에 적용
# 각 픽셀 값을 테이블 기반으로 변환해 보정된 이미지 생성
img2 = cv2.LUT(img, table)

# 원본 이미지와 보정된 이미지를 위아래로 합침(vstack) -> 이미지 2개 보여주기
res = np.vstack((img,img2))

cv2.imshow("result g=1.7",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
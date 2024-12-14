# 다음과 같은 커널을 직접 정의하고 그 커널을 사용한 필터를 shapes.jpg에 적용
# 그리고 opencv의 laplacian 필터와 비교한다.

import cv2
import numpy as np

img = cv2.imread("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/shapes.png", cv2.IMREAD_GRAYSCALE)
kernel=np.array(
    [[0,1,1,2,2,2,1,1,0],
     [1,2,4,5,5,5,4,2,1],
     [1,4,5,3,0,3,5,4,1],
     [2,5,3,-12,-24,-12,3,5,2],
     [2,5,0,-24,-40,-24,0,5,2],
     [2,5,3,-12,-24,-12,3,5,2],
     [1,4,5,3,0,3,5,4,1],
     [1,2,4,5,5,5,4,2,1],
     [0,1,1,2,2,2,1,1,0]],
     dtype=np.float32)
print(np.sum(kernel))

# 사용자 정의 커널, 커널 중심의 음수 값과 주변 양수 값을 통해 특정 에지 강조 효과를 적용
# filter2D 함수로 필터링 수행
img1 = cv2.filter2D(img, cv2.CV_8U, kernel)

# 2차 미분을 사용하여 이미지의 에지를 강조
# laplacian 함수로 에지 추출
img2 = cv2.Laplacian(img, cv2.CV_8U, ksize=9)

cv2.imshow("origin", img)
cv2.imshow("filter2d", img1)
cv2.imshow("laplacian", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

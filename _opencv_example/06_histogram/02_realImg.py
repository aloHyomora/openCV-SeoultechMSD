import cv2
import numpy as np

def equalize(img, maxv):
    rows, cols = img.shape
    freq = cv2.calcHist([img], [0], None, [maxv+1], [0,maxv])
    prob = freq.ravel() / (rows*cols)
    pdf = np.cumsum(prob)
    
    # CDF 값을 이미지의 밝기 범위(0~maxv)로 정규화하여 새로운 픽셀 값을 생성 
    table = np.round(pdf*maxv).astype(np.uint8)
    return table[img]

originalImg = cv2.imread("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/bigben.jpg", cv2.IMREAD_GRAYSCALE)
equal = equalize(originalImg, 255)
combineImg = np.vstack((originalImg, equal))
cv2.imshow('origin-equalized', combineImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

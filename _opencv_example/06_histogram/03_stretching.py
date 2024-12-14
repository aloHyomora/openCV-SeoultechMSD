import cv2
import numpy as np
def equalize(img,maxv):
    rows, cols = img.shape
    freq = cv2.calcHist([img], [0], None, [maxv+1], [0, maxv])
    prob = freq.ravel()/(rows* cols)
    pdf = np.cumsum(prob)
    table=np.round(pdf*maxv).astype(np.uint8)
    return table[img]
def stretching(img,maxv):
    return cv2.normalize(img, None, 0, maxv-1, cv2.NORM_MINMAX)

org=cv2.imread('C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/hill.jpg',cv2.IMREAD_GRAYSCALE)
equal=equalize(org,256)
stretch=stretching(org,256)
combi=np.hstack((org,equal,stretch))
cv2.imshow('Original-Equalized-Streching',combi)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np
import matplotlib.pyplot as plt

def generateBigImg(img):
    
    # 400x400으로 확대, interpolation: 픽셀 값을 평균화하여 부드럽게 확대, 각 픽셀 값을 36배 해서 밝기 강조
    im = cv2.resize(img, (400,400), interpolation=cv2.INTER_AREA)*36
    rows, cols = img.shape
    print(rows,cols)
    for r in range(rows):
        for c in range(cols):
            r0,r1,c0,c1=100*r,100*(r+1),100*c,100*(c+1)
            color = (255,255,255) if img[r,c]<4 else (0,0,0)
            cv2.putText(im, f'{img[r,c]}', (c0+40,r0+60), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 1, cv2.LINE_AA)
            
    return im

def generateBigImg2(img):
    im = np.zeros((400,400),np.uint8)
    rows, cols = img.shape
    for r in range(rows):
        for c in range(cols):
            r0, r1, c0, c1 = 100*r,100*(r+1),100*c,100*(c+1)
            v = img[r,c]
            im[r0:r1,c0:c1] = v*36
            color = (255,255,255) if v<4 else (0,0,0)
            cv2.putText(im,f'{v}',(c0+40,r0+60),cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    color, 1,cv2.LINE_AA)
    return im



small = np.array([[0,1,1,1], [1,3,1,6], [5,6,6,6], [2,4,4,4]], dtype=np.uint8)
big = generateBigImg(small)
# big = generateBigImg2(small)

# 입력 배열: small, 계산할 채널: 0(그레이스케일 이미지는 0번 채널), 마스크(전체 이미지를 사용하므로 None), 히스토그램의 bin 개수, 히스토그램 값의 범위(0~8)
# 0~7 범위에 해당하는 값들의 빈도수가 반환됨.
freq = cv2.calcHist([small], [0], None, [8], [0,8])
print(freq)
cv2.imshow('big image', big)
# freq.ravel(): freq 배열을 1차원으로 펼쳐 y축 값으로 사용(각 값의 빈도수).
plt.bar(range(8), freq.ravel())
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
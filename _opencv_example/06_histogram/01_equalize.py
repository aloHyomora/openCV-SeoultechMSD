import cv2
import numpy as np

# 히스토그램 평활화는 이미지의 밝기(픽셀 값) 분포를 재조정하여, 이미지의 대비를 개선하는 기법입니다. 
# 밝기 값의 히스토그램을 평평하게 만들어 이미지의 어두운 영역과 밝은 영역이 좀 더 잘 보이도록 만듭니다.

def genBigImg(simg):
    im = cv2.resize(simg, (400,400), interpolation=cv2.INTER_AREA)*36
    rows,cols  = simg.shape
    for r in range(rows):
        for c in range(cols):
            r0,r1,c0,c1 = 100*r,100*(r+1),100*c,100*(c+1)
            color = (255,255,255) if simg[r,c]<4 else (0,0,0)
            cv2.putText(im,f'{simg[r,c]}',(c0+40,r0+60),cv2.FONT_HERSHEY_SIMPLEX, 0.8, 
                color,1,cv2.LINE_AA)
    return im

def equalize(img, maxv):
    rows, cols = img.shape
    # 각 픽셀 값(0~maxv)의 빈도수를 반환, freq는 각 밝기 값에 해당하는 빈도수를 갖는 배열입니다.
    freq = cv2.calcHist([img], [0], None, [maxv+1], [0, maxv])
    
    # 각 픽셀 값의 빈도수를 확률로 정규화, 결과: 픽셀 값의 확률 분포 prob
    prob = freq.ravel()/(rows* cols)
    
    # 확률의 누적합(CDF)를 계산
    cdf = np.cumsum(prob)
    
    # CDF를 최대값으로 정규화하여 LUT 생성, LUT는 기존 픽셀 값을 새로운 값으로 매핑하는 테이블
    table=np.round(cdf*maxv).astype(np.uint8) #LUT 생성
    return table[img]    

small = np.array([[0,1,1,1],[1,3,1,6],[5,6,6,6],[2,4,4,3]], dtype=np.uint8)
big = genBigImg(small)

small_eq = equalize(small, 7)
big_eq = genBigImg(small_eq)

cv2.imshow('Original', big)
cv2.imshow('Equalized', big_eq)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

def genColored(simg, sz):
    im = np.zeros((sz[1],sz[0],3), np.uint8)
    rows, cols = simg.shape[:2]
    print(rows, cols)
    dc=sz[0]//cols
    dr=sz[1]//rows
    
    for r in range(rows):
        for c in range(cols):
            r0,r1,c0,c1=dr*r,dr*(r+1),dc*c,dc*(c+1)
            value = simg[r,c]            
            im[r0:r1,c0:c1] = colors[value]
            color=(255,255,255) if value==0 else (0,0,0)
            cv2.putText(im,f'{value}',(c0+40,r0+60),cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    color, 1,cv2.LINE_AA)
    return im

colors=[(0,0,0),(0,255,0),(128,128,0),(0,128,128),(128,0,128),(0,0,255),(255,0,0)]
img = np.array([[0, 0, 1, 1, 0, 0, 0, 0, 0],
                    [1, 1, 1, 1, 0, 0, 1, 0, 0],
                    [1, 1, 1, 1, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 1, 1, 0, 1],
                    [0, 0, 0, 1, 1, 1, 1, 0, 1],
                    [0, 0, 0, 1, 0, 0, 1, 0, 1],
                    [0, 0, 1, 1, 1, 1, 1, 0, 1],
                    [0, 0, 0, 0, 1, 0, 0, 0, 0]], dtype= np.uint8)

big=genColored(img,(900,800))
cv2.imshow('binary', big)
n, labels = cv2.connectedComponents(img)
print(n)
print(labels)

colored=genColored(labels,(900,800))
cv2.imshow('Color labeled', colored)
cv2.waitKey(0)
cv2.destroyAllWindows()
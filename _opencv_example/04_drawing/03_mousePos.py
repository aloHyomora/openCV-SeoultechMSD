import cv2
import numpy as np

def onMouse(event, x, y, flags, parm):
    global img
    if event == cv2.EVENT_MOUSEMOVE:
        img[:,:,:]=0
        cv2.putText(img, f'({x},{y})',(20,20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, white, 1, cv2.LINE_AA)
        cv2.circle(img, (x, y), 8, (0,255,0), -1)        

white = (255,255,255)
img = np.zeros((500,500,3), dtype=np.uint8)
cv2.namedWindow("window")
cv2.setMouseCallback("window",onMouse)
while cv2.waitKey(30) != 27:
    cv2.imshow("window", img)
    
cv2.destroyAllWindows()
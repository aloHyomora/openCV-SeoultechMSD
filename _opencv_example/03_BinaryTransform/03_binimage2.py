import cv2

def onChange(val):
    global threshold
    threshold = val

threshold = 128

image_path = "Images/coins.jpg"
img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('coins', 0)
cv2.createTrackbar('Threshold', 'coins', 0, 255, onChange)
cv2.setTrackbarPos('Threshold', 'coins', threshold)
while cv2.waitKey(1) != 27: # ESC key to exit
    _, img_b = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY)
    cv2.imshow("coins", img_b)
    
cv2.destroyAllWindows()

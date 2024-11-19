import cv2

image_path = "Images/lena.jpg"
img = cv2.imread(image_path)
cv2.imshow("lena", img)

x, y, width, height = cv2.selectROI("lena", img)
roi = img[y:y+height,x:x+width]
roi_grey = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

res, roi_binary = cv2.threshold(roi_grey, 150, 255, cv2.THRESH_OTSU)

cv2.imshow("roi",roi_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()
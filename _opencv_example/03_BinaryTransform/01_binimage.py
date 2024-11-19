import cv2
 
img_path = "images/lego.jpg"
img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)

# threshold를 기준으로 image 처리 가능
threshold = 183
img[img>threshold] =255
img[img<threshold] =0


# 이미지가 제대로 읽혔는지 확인
if img is None:
    print("Image not found.")
else:
    cv2.imshow('img',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
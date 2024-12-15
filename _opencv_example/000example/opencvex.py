import cv2
import os
import random

def select_random_image(folder_path):
    # 폴더 내 모든 파일 가져오기
    files = os.listdir(folder_path)

    # 이미지 파일 필터링 (jpg, png, bmp 등)
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']
    image_files = [file for file in files if os.path.splitext(file)[1].lower() in image_extensions]

    # 이미지 파일이 없으면 종료
    if not image_files:
        print("이미지 파일이 없습니다.")
        return None

    # 랜덤으로 이미지 파일 선택
    selected_image_file = random.choice(image_files)
    selected_image_path = os.path.join(folder_path, selected_image_file)

    # OpenCV로 이미지 읽기
    image = cv2.imread(selected_image_path)
    if image is None:
        print("이미지를 읽을 수 없습니다.")
        return None

    print(f"랜덤으로 선택된 이미지: {selected_image_file}")
    return image

# 폴더 경로 지정
folder_path = "C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images"  # 실제 폴더 경로로 변경
loaded_image = select_random_image(folder_path)

cv2.imshow("Randomly Selected Image", loaded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 1. 이미지를 읽고 그레이스케일로 변환한 후, 원본 이미지와 그레이스케일 이미지를 화면에 출력하세요.
# 힌트: cv2.imread와 cv2.cvtColor를 사용하세요.
img1 = select_random_image(folder_path)
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #(cv2.COLOR_RGB2GRAY)

cv2.imshow("gray", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. 이미지를 원래 크기의 절반으로 축소
# cv2.resize
img3 = select_random_image(folder_path)
img4 = cv2.resize(img3, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imshow('resized img',img4)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3. 빈 이미지를 생성한 뒤, 이미지 중앙에 빨간색 원을 그리세요.
# 힌트: np.zeros와 cv2.circle을 사용하세요.
import numpy as np
img5 = np.zeros((500,500,3), dtype=np.uint8)
center_x, center_y = img5.shape[1]//2, img5.shape[0]//2

radius = 100
color = (0,0, 255)
thickness = -1

img6 = cv2.circle(img5, (center_x,center_y),radius, color, thickness)
img7 = np.vstack((img5,img6))
cv2.imshow("Image with circle", img7)
cv2.waitKey(0)
cv2.destroyAllWindows()

img8 = select_random_image(folder_path)
edges = cv2.Canny(img8, 50, 100)
#img9 = np.vstack((img8, edges))
cv2.imshow("Canny", edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

img9 = select_random_image(folder_path)
blurred_imgae = cv2.GaussianBlur(img9, ksize=(5,5), sigmaX=0)
cv2.imshow("blurred_imgae", blurred_imgae)
cv2.waitKey(0)
cv2.destroyAllWindows()

img10 = select_random_image(folder_path)
img11 = cv2.cvtColor(img10, cv2.COLOR_BGR2GRAY)
_, bin_img = cv2.threshold(img11, 127, 255, cv2.THRESH_BINARY)
cv2.imshow("binary", bin_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7. 이진화된 이미지에 모폴로지 연산(예: 팽창)을 적용하세요.
# 힌트: cv2.dilate를 사용하세요.
image1 = select_random_image(folder_path)
image2 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)

_, binary_image = cv2.threshold(image2, 127, 255, cv2.THRESH_BINARY)

kernel = np.ones((3,3), np.uint8)
dilated_image = cv2.dilate(binary_image, kernel, iterations=1)

cv2.imshow("Dilated Image", dilated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8.이진화된 이미지에서 외곽선을 검출하고 이를 원본 이미지 위에 그리세요.
# 힌트: cv2.findContours와 cv2.drawContours를 사용하세요.
image3 = select_random_image(folder_path)
image4 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY) # 그레이스케일로 변환
_, binimg = cv2.threshold(image4, 127,255,cv2.THRESH_BINARY)    
contours, _ = cv2.findContours(binimg, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = image3.copy()
cv2.drawContours(contour_image, contours, -1, (0,255,0), 2)

cv2.imshow("contours", contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Harris 코너 검출을 사용하여 이미지의 코너를 찾아 표시하세요.
# cv2.cornerHarris
image5 = select_random_image(folder_path)
image6 = cv2.cvtColor(image5, cv2.COLOR_BGR2GRAY)
# Harris 코너 검출
gray = np.float32(image6)
corner_response = cv2.cornerHarris(gray, blockSize=2, ksize=3, k=0.04)

corner_threshold = 0.01*corner_response.max()
image5[corner_response>corner_threshold] = [0,0,255]
cv2.imshow("image with corners",image5)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 12. 이미지를 BGR 채널로 분리한 뒤 각 채널을 개별적으로 출력하세요.
# 힌트: cv2.split을 사용하세요.
chimage = select_random_image(folder_path)
blue_channel, green_channel, red_channel = cv2.split(chimage)

# 각 채널을 컬러 이미지로 변환
blue_img = cv2.merge([blue_channel, np.zeros_like(blue_channel), np.zeros_like(blue_channel)])
green_img = cv2.merge([np.zeros_like(green_channel), red_channel, np.zeros_like(green_channel)])
red_img = cv2.merge([np.zeros_like(red_channel), np.zeros_like(red_channel), red_channel])

stacked_img = np.vstack((blue_img,green_img,red_img))
cv2.imshow("bgr",stacked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 문제 14: 이미지에서 허프 선 변환을 사용해 직선을 검출하세요.
# 힌트: cv2.HoughLines를 사용하세요.
ima = select_random_image(folder_path)
grayima = cv2.cvtColor(ima,cv2.COLOR_BGR2GRAY)
edge = cv2.Canny(grayima, 50,150,apertureSize=3)
lines = cv2.HoughLines(edge, rho=1, theta=np.pi/180, threshold=150)
if lines is not None:
    for line in lines:
        rho, theta = line[0]
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho            
        x1 = int(x0 + 1000 * (-b))  # 선의 끝점 계산
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(ima, (x1, y1), (x2, y2), (0, 0, 255), 2)  # 빨간색 직선

cv2.imshow("Edges", edge)
cv2.imshow("Hough Lines", ima)
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2
import numpy as np

# 비디오 파일 열기
cap = cv2.VideoCapture("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/video/fish_tank.mp4")

# 첫 번째 프레임 읽기
ret, frame = cap.read()

# 첫 번째 프레임을 그레이스케일로 변환
prv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# HSV 이미지 초기화 (BGR 이미지와 동일한 크기)
hsv = np.zeros_like(frame)

# HSV 이미지의 채도를 최대값으로 설정 (255)
hsv[:, :, 1] = 255

flow = None  # Optical Flow를 저장할 변수 초기화

# 프레임을 반복해서 처리
while True:
    ret, frame = cap.read()  # 다음 프레임 읽기
    if ret:
        # 현재 프레임을 그레이스케일로 변환
        next_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Farneback Optical Flow 계산
        flow = cv2.calcOpticalFlowFarneback(
            prv_img, next_img, None,  # 이전 프레임, 현재 프레임
            0.5,  # 피라미드 스케일
            3,    # 피라미드 레벨 수
            15,   # 윈도우 크기
            3,    # 반복 횟수
            5,    # 다항식 확장 크기
            1.2,  # 다항식 표준 편차
            0     # 플래그 (기본값)
        )

        # Optical Flow에서 x, y 벡터를 크기(magnitude)와 각도(angle)로 변환
        mag, ang = cv2.cartToPolar(flow[:, :, 0], flow[:, :, 1])

        # HSV 이미지의 Hue 값을 Optical Flow 각도로 설정 (0~360도)
        hsv[:, :, 0] = np.rad2deg(ang)

        # HSV 이미지의 Value 값을 Optical Flow 크기로 설정 (정규화하여 0~255 사이 값)
        hsv[:, :, 2] = cv2.normalize(mag, None, 0, 255, cv2.NORM_MINMAX)

        # HSV 이미지를 BGR 형식으로 변환
        bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

        # 원본 프레임과 Optical Flow 결과를 수직으로 쌓아서 하나의 이미지로 표시
        res = np.vstack((frame, bgr))

        # 결과 이미지 출력
        cv2.imshow('Result', res)

        # 현재 프레임을 이전 프레임으로 업데이트
        prv_img = next_img
    else:
        break

    # ESC 키를 누르면 루프 종료
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

# 비디오 캡처 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
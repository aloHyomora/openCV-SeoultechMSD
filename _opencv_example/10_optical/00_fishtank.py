import numpy as np
import cv2

# 설정된 최대 추적 점의 수
numOfConner = 100

# 비디오 파일 열기
cap = cv2.VideoCapture("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/video/fish_tank.mp4")  # 비디오 파일 경로

# 코너 검출 (goodFeaturesToTrack)의 파라미터 설정
feature_params = {
    'maxCorners': numOfConner,  # 최대 추적할 코너 점 수
    'qualityLevel': 0.2,        # 코너 품질 수준 (0~1)
    'minDistance': 10,          # 최소 점 간 거리
    'blockSize': 7              # 코너 검출 블록 크기
}

# Lucas-Kanade Optical Flow의 파라미터 설정
lk_params = {
    'winSize': (15, 15),        # 검색 윈도우 크기
    'maxLevel': 2,              # 피라미드 레벨 수
    'criteria': (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03)  # 종료 기준
}

# 점 추적 시각화를 위한 무작위 색상 생성
color = np.random.randint(0, 255, (numOfConner, 3))

# 첫 프레임 읽기 및 그레이스케일로 변환
ret, old_frame = cap.read()
prev_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

# 초기 코너 검출
prev_pts = cv2.goodFeaturesToTrack(prev_gray, mask=None, **feature_params)

# 추적 선을 그리기 위한 빈 마스크 이미지
mask = np.zeros_like(old_frame)

# 비디오 프레임 루프
while True:
    ret, frame = cap.read()
    if not ret:  # 비디오 종료 시 루프 탈출
        break

    # 현재 프레임을 그레이스케일로 변환
    new_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Lucas-Kanade Optical Flow를 사용하여 점 이동 계산
    # Lucas-Kanade Optical Flow를 계산, 이전 프레임의 점들이 현재 프레임에서 어디로 이동했는지 추적합니다.
    new_pts, st, err = cv2.calcOpticalFlowPyrLK(prev_gray, new_gray, prev_pts, None, **lk_params)

    # 점 이동 경로 시각화, 이동 성공한 점 필터링
    good_new = new_pts[st == 1]
    good_prev = prev_pts[st == 1]

    # 이전 점과 현재 점을 선으로 연결
    for i, (new, old) in enumerate(zip(good_new, good_prev)):
        new_i = new.astype(np.int16)  # 새로운 점 좌표 정수화
        old_i = old.astype(np.int16)  # 이전 점 좌표 정수화

        # 이동 경로 선 그리기
        cv2.line(mask, old_i, new_i, color[i].tolist(), 2)

        # 현재 점을 원으로 표시
        cv2.circle(frame, new_i, 5, color[i].tolist(), -1)

    # 이동 경로를 현재 프레임에 오버레이
    img = cv2.add(frame, mask)

    # 결과 출력
    cv2.imshow('frame', img)

    # ESC 키를 누르면 종료
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

    # 이전 프레임 및 점 업데이트
    prev_gray = new_gray.copy()
    prev_pts = good_new.reshape(-1, 1, 2)

# 비디오 캡처 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()

import cv2
import numpy as np

# Optical Flow 결과를 시각화하는 함수
def draw_flow(img, flow, step=16):
    # 이미지의 높이와 너비 가져오기
    h, w = img.shape[:2]
    
    # 격자점 생성: step 간격으로 행(y), 열(x) 좌표를 생성
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2, -1).astype(np.int32)
    
    # 격자점에서 Optical Flow 값(vx, vy)을 추출 (8배 확대)
    vx, vy = flow[y, x].T * 8  
    
    # 격자점과 이동 후 점의 좌표를 라인 데이터로 변환
    lines = np.vstack([x, y, x+vx, y+vy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)  # 소수점 반올림
    
    # Optical Flow를 라인으로 시각화
    cv2.polylines(img, lines, 0, (0, 0, 255), 2)  # 빨간색 라인
    
    # 시작 점(격자점)을 초록색 원으로 표시
    for (x1, y1), (_x2, _y2) in lines:
        cv2.circle(img, (x1, y1), 1, (0, 255, 0), 1)
    
    return img  # 시각화된 이미지 반환

# 비디오 파일 열기
cap = cv2.VideoCapture("C:/Users/aloho/Github/openCV-SeoultechMSD/_opencv_example/Images/video/fish_tank.mp4")

# 첫 번째 프레임 읽기
ret, frame = cap.read()

# 첫 번째 프레임을 그레이스케일로 변환
prv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# 프레임 반복 처리
while True:
    ret, frame = cap.read()  # 다음 프레임 읽기
    if ret:
        # 현재 프레임을 그레이스케일로 변환
        next_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Optical Flow 계산 (Farneback 알고리즘 사용)
        flow = cv2.calcOpticalFlowFarneback(
            prv_img, next_img, None, 0.5, 3, 15, 3, 5, 1.2, 0
        )
        
        # Optical Flow 시각화
        res = draw_flow(frame, flow)
        
        # 결과 출력
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

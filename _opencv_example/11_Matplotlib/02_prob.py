import matplotlib.pyplot as plt
import numpy as np

# 빈 리스트 생성 (주사위 결과를 저장)
res = []

# 10만 번 반복하여 7개의 주사위를 굴리고 그 합계를 리스트에 추가
for _ in range(100000):
    dices = np.random.randint(1, 7, 7)  # 7개의 주사위에서 나오는 값을 생성 (1~6 사이 정수)
    res.append(dices.sum())  # 주사위 값의 합계를 결과 리스트에 추가

# 히스토그램을 생성
# n은 빈도수, bins는 히스토그램 구간, _는 막대의 정보를 반환
n, bins, _ = plt.hist(res, bins=range(7, 43), density=True, facecolor='g', alpha=0.3)

# 데이터의 평균과 표준편차 계산
m, sig = np.mean(res), np.std(res)

# 정규분포 PDF 계산
x = np.array(range(51))  # 0부터 50까지의 정수 배열 생성
pdf = 1 / (sig * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x - m) / sig) ** 2)  # 정규분포 식
print(pdf)

# PDF를 빨간색 선으로 그리기
plt.plot(x, pdf, 'r')

# 평균과 표준편차 범위 표시를 위한 점선 추가
p = [m - sig, m, m + sig]  # 평균 - 표준편차, 평균, 평균 + 표준편차 값
y = [0, 0.1]  # 수직선의 y 값 범위
plt.plot([p[0], p[0]], y, 'k:',  # 평균 - 표준편차를 나타내는 검은색 점선
         [p[1], p[1]], y, 'b:',  # 평균을 나타내는 파란색 점선
         [p[2], p[2]], y, 'k:')  # 평균 + 표준편차를 나타내는 검은색 점선

# x축의 범위를 7에서 42로 제한 (7은 7개의 주사위에서 최소 값, 42는 최대 값)
plt.xlim([7, 42])

# 그래프 표시
plt.show()

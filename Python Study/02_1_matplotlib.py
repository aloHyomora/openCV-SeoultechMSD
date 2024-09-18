# x가 0에서 4까지 0.1 간격으로 변할 때 다음 수식에 대한 그래프를 그려라. 단, matplotlib의 pyplot을 이용한다.
import matplotlib.pyplot as plt

X = [e/10 for e in range(41)]
Y = []

for x in X:
    y = x**3 - 3*x**2 - 7
    Y.append(y)
    print(f'f({x}) = {y:.3f}')
plt.plot(X,Y)
plt.grid()
plt.show()
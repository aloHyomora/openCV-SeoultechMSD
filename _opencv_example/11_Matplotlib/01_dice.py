# 한꺼번에 주사위 7개를 던져 합을 구한다고 하자. 100,000번 던졌을 때에 합에 대한 돗수분포를 그려라. 이때 합의 범위는 7에서 42까지가 될 것이다.
import matplotlib.pyplot as plt
import numpy as np

res = []
for _ in range(100000):
    dices = np.random.randint(1,7,7)
    res.append(dices.sum())
h, bins,_=plt.hist(res, bins=range(7,43),density=False,facecolor='g', alpha=0.3)
plt.plot(bins[:-1],h,'-o')
plt.show()
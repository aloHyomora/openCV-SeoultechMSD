import numpy as np

for ABCD in range(1000,10000):
    AB = ABCD // 100
    CD = ABCD % 100
    if ABCD == AB**2 + CD**2:
        print(ABCD)
    
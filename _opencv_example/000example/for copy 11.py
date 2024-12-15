import random as rnd

A = list(range(1,21))
B = list(range(1,21))
L = []

for a in A:
    b = a
    while a==b:
        b = rnd.choice(B)
    L.append((a,b))    
    B.remove(b)
    
print(L)    
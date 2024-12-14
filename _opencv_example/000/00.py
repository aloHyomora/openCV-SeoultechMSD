import numpy as np

res = []
for a in range(ord('z'),ord('a')-1, -1):
    res.append((chr(a)))
    
print(res)

res2 = []
for a in range(1,21):
    res2.append(a**3)
    
print(res2)

res3 = []
A = list(range(ord('a'), ord('z')+1)) + list(range(ord('A'),ord('Z')+1))
for a in A:
    res3.append(chr(a))
    
print(res3)

D={}
for i in range(len(res3)):
    D[i]=res3[i]
    
print(D)
    
D1 = {}
for i in range(1,10):
    for j in range(1,10):
        D1[f'{i}x{j}']=i*j
print(D1)

import random

A0 = list(range(1,21))
B0 = list(range(1,21))
random.shuffle(B0)
L = []
for i in range(len(A0)):
    L.append((A0[i],B0[i]))
print(L)

oneP = 3.30579
PY = list(range(30,51))
M2 =[]
for py in range(30,51):
    M2.append(py*oneP)

for i in range(len(PY)):
    print(f'{PY[i]}평: {M2[i]:7.2f}m2')
    
L=[1,2,7,4,7,4,7,1,2,4]
for e in [4,7]:
    while e in L:
        L.remove(e)

print(L)

s="2024년 1월 1일 새해."
cnt_a,cnt_d = 0,0
for c in s:
    if c.isalpha():
        cnt_a+=1
    elif c.isdigit():
        cnt_d += 1
print(s)
print(f'문자: {cnt_a}, 숫자: {cnt_d}')
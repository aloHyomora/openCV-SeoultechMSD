ch= ['해','달','솔','길','숲','별','강','비','숨','꿈','빛']
L = []
for first in ch:
    for second in ch:
        L.append(first+second)
        
print(L)
name=[a+b for a in ch for b in ch if a!=b]
print(name)
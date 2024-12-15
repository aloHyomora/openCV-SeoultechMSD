for i in range(2000, 3001):
    d1 = i % 10
    d10 = (i // 10) % 10
    d100 = (i // 100) % 10
    d1000 = (i // 1000) % 10
    sum = d1 + d10 + d100 + d1000
    if sum == 7:
        print(i)
        
print()        
for n in range(2000,3001):
    sum = 0
    for x in range(4):
        sum += (n // 10**x)%10    
    if sum == 7:
        print(n)
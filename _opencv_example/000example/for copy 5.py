import time

def show(n):
    for b in range(4):
        print('●' if n & (1<<b) != 0 else '○', end='')
    time.sleep(0.1)
    print()
    
m=1
while True:
    for _ in range(3):
        m <<= 1
        show(m)
    for _ in range(3):
        m >>= 1
        show(m)
        
# 1인 비트 자리수 출력
n = int(input('정수를 입력하세요'))
bits = n.bit_length()
print(bin(n), bits)

for i in range(bits):
    if n & 1 << i:
        print(i)
    
for i, c in enumerate(bin(n)[2:]):
    if c == '1':
        print(bits -1 - i)
# 연산자 레벨 2

# 2000부터 3000까지의 정수 중 모든 자리수의 합이 7이 되는 수들을 모두 출력하라.
for number in range(2000,3001):
    sum = 0
    for x in range(4): # 4번 반복
        sum += (number // 10**x) % 10
    if sum == 7:
        print(number)

# 임의의 정수를 입력받아 2진수로 변환했을 때 1인 비트 자리수를 출력하라.
# 힌트 비트 연산자 << 로 마스크를 만들어 해결하자.
n= input('임의의 정수를 입력하세요.:')
binNum = bin(n)
bits = n.bit_length() # n을 이진수로 표현할 때 필요한 비트 수 계산

for i in range(bits):  # 비트 수만큼 반복
    if n & 1<<i: # n의 i번째 비트가 1인지 확인
        print(i)
print("==== 다른 방법 ====")
bits = n.bit_length()  # n을 이진수로 표현할 때 필요한 비트 수 계산
for i, c in enumerate(bin(n)[2:]):  # 이진수의 두 번째 자리부터 하나씩 읽기
    if c == '1':  # 이진수에서 '1'이면
        print(bits - 1 - i)  # 해당 비트의 위치 출력(0번 비트가 가장 오른쪽 비트)

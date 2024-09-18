# 4개의 LED가 있을 때, 상태를 켜짐, "●” , 꺼짐  "○” 로 표시하여 한 개의 켜진 LED가 좌우로 왕복하도록 만든다.  즉 ,   LED가 ●○○○ 가 ○○○● 까지 왕복한다.
# > while 문으로 무한 반복시키고 m=1을 <<, >> 연산자로 이용하여 이진수 패턴을 만든다.
# 💡 time 모듈의 sleep(s) 는 s초만큼 지연시킨다.
import time
def show(n):
    for b in range(4):
        print('●' if n & (1<<b) != 0 else '○',end='')
    time.sleep(0.5)
    print()
    
m = 1
while True:
    # 종료 여부를 확인하는 입력 받기
    exit_input = input("종료하려면 'q'를 입력하세요. 계속하려면 Enter: ")
    if exit_input.lower() == 'q':  # 'q'를 입력하면 프로그램 종료
        print("프로그램을 종료합니다.")
        break  # while 루프를 빠져나감
    
    for _ in range(3):
        m = m << 1
        show(m)
    for _ in range(3):
        m >>= 1
        show(m)

# 다음 식을 만족하는 4자리 정수 ABCD를 모두 구하라.
# $AB^2+CD^2=ABCD$
# 단, A, B, C, D는 각각 1자리 정수이고 A=1, B=2 라면 AB2는 122을 의미한다. ABCD가 0,1인 경우는 구하지 않는다.
for ABCD in range(10000):
    AB = ABCD // 100
    CD = ABCD % 100
    if ABCD == AB**2 + CD**2:
        print(ABCD)

#1에서 100까지 정수에서 13의 배수 또는 5의 배수인 수를 모두 출력하고 총합을 구하는 프로그램을 for 문으로 작성하라.
for n in range(1, 101):
    if n % 13 == 0 or n % 5 == 0:
        print(n)
        
# 다음과 같이 주어진 수열의 1에서 10항까지 합을 구하자.
# a_{n+1}=2a_n+1,   n>0
# a_0=0
sum = 0
an_1 = 0
for k in range(1,11):
    an = 2 * an_1 + 1
    sum += an
    an_1 = an
    print(f'{k} : {an}')
print(f'합 = {sum}')

level = 5
for i in range(level):
    for j in range(level - i, 0, -1):
        print(f'{j} ',end='')
    print()
    
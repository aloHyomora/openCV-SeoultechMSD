# -*- coding: utf-8 -*-

import math # 수학 계산 라이브러리

class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1. [2진수를 input으로 받아 10진수와 16진수 출력]",
            "프로그램 2: [반경 r을 입력 받아 구의 표면적과 체적을 출력]",
            "프로그램 3: [직각삼각형의 밑변과 높이를 입력 받아서 빗변과 밑변과 빗변의 사이각을 구함. 단, 사이각은 °로 출력]",
            "프로그램 4: [임의의 정수를 입력받아 2진수로 변환했을 때 1인 비트 자리수를 출력. 비트 연산자 << 로 마스크를 만들기]",
            "프로그램 5: [2000부터 3000까지의 정수 중 모든 자리수의 합이 7이 되는 수들을 모두 출력]",
            "프로그램 6: [통신 오류를 감지하기 위하여 데이터의 모든 문자의 아스키 코드에 대하여 비트 배타적 논리합 (xor)을 구하여 맨 뒤에 16진수로 2개의 문자를 붙여 전송한다. 이를 BCC(block check code)라 부른다. 수신된 데이터의 BCC를 계산해보고 마지막에 수신한 BCC와 일치하지 않으면 오류인 것이다. 여기서는 수신한 데이터가 Hello python!이라고 가정하고 그 BCC를 구하는 프로그램을 작성해보자.]",
            "프로그램 7: [[turtle]  관람차 그리기]"
        ]
    def program_1(self):
        print()
        print("프로그램 1을 시작합니다...")
        inputData = input('2진수를 입력하세요.')
        print(int(inputData, base=2)) # 2진수를 10진수 출력
        print(hex(int(inputData, base=2))[2:]) # 2진수를 16진수로 출력
    
    def program_2(self):
        print()
        print("프로그램 2을 시작합니다...")
        radius = float(input('반경 r을 입력하세요:'))
        print(f"표면적은 4 x pi x r^2 = {4 * math.pi * math.pow(radius, 2)} 체적은 4 / 3 * pi x r^3 = {4 / 3  * math.pi * math.pow(radius, 3)}")
                
    def program_3(self):
        print()
        print("프로그램 3을 시작합니다...")
        width = float(input('밑변을 입력하세요:'))
        height = float(input('높이를 입력하세요:'))
        
        hypotenuse = math.sqrt(height**2 + width**2)
        seta = math.atan(height/width) * 180 / math.pi
        
        print(f'삼각형의 빗변은 {hypotenuse:.4f}이고, 삼각형의 사이각은 {seta:.4f}이다.')
        
    def program_4(self):
        print()
        print("프로그램 4을 시작합니다...")
        inputData2 = int(input('임의의 정수를 입력하세요:'))
        print(bin(inputData2))
        
        bitsNum = inputData2.bit_length()
        for i in range(bitsNum):
            if inputData2 & 1 << i:
                print(i + "번 인덱스")
        print("=======다른 방법=======")        
        bitsNum2 = inputData2.bit_length()
        for i, c in enumerate(bin(inputData2)[2:]):  # enumerate() 문자열에서 각 자리의 인덱스와 해당 자리의 값을 반환한다.
            if c == '1':
                print(bitsNum2 - 1 - i)
        
    def program_5(self):
        print()
        print("프로그램 5을 시작합니다...") 
        
        # // 연산자 -> 소수점을 버리고 결과를 반환
        for number in range(2000, 3001):
            d1 = number % 10
            d10 = (number // 10) % 10
            d100 = (number // 100) % 10
            d1000 = (number // 1000) % 10
            sum = d1 + d10 + d100 + d1000
            if sum == 7:
                print(number)
        print("=======다른 방법=======")            
        for n in range(2000,3001):
            sum = 0
            for x in range(4):
                sum += (n // 10**x) % 10
            if sum == 7:
                print(n)
    def program_6(self):
        print()
        print("프로그램 6을 시작합니다...")  
        data ="Hello python!"
        bcc=0
        for c in data:
            bcc^=ord(c)  #비트 배타적 논리합 XOR 연산은 두 비트를 비교하여 두 비트가 다르면 1, 같으면 0을 반환
            bcc_s= hex(bcc)[2:].zfill(2) # zero fill
            print(data+bcc_s)
        
    def program_7(self):
        print()
        print("프로그램 7을 시작합니다...")  
        
        import turtle
        import random as rnd
        
        turtle1 = turtle.Turtle()
        screen = turtle.Screen()
        
        screen.setup(500,500)
        screen.tracer(0)
        
        for i in range(13):
            turtle1.pencolor(rnd.random(), rnd.random(), rnd.random())
            turtle1.width(5)            
            
            turtle1.pu()
            turtle1.goto(0,0)
            turtle1.pd()
                                
            turtle1.forward(150)
            turtle1.right(90); turtle1.forward(15)
            turtle1.left(90); turtle1.forward(30)
            turtle1.left(90); turtle1.forward(30)
            turtle1.left(90); turtle1.forward(30)
            turtle1.left(90); turtle1.forward(15)
            turtle1.right(90); turtle1.forward(150)
                        
            turtle1.right(30)
            

    def call_method(self, method_string):
        if method_string.strip().startswith("program"):
            try:
                number = int(method_string.split("_")[1])  # 프로그램 번호 가져오기
                if 1 <= number <= self.get_program_count():
                    print()
                    print(self.programs[number - 1])  # 프로그램 출력
                    method = getattr(self, f"program_{number}", None)
                    if method:
                        method()  # 해당 메서드 실행
                    else:
                        print(f"Error: program_{number} 메서드가 정의되지 않았습니다.")
                else:
                    print(f"유효하지 않은 프로그램 번호입니다: {number}")
            except (IndexError, ValueError):
                print(f"문자열 형식이 올바르지 않습니다: {method_string}")
        else:
            print(f"유효하지 않은 메서드 이름입니다: {method_string}")
        
    def get_program_count(self):
        return len(self.programs)

    def show_all_program(self):
        for program in self.programs:
            print(program)

    def show_program(self, number):        
        if 1 <= number <= self.get_program_count():
            print(self.programs[number - 1])
        else:
            print(f"유효하지 않은 번호입니다. 1에서 {self.get_program_count()} 사이의 숫자를 입력하세요.")
    
    

# 클래스 인스턴스 생성
example = ExampleClass()

while True:
    try:
        count = example.get_program_count()  # 프로그램 개수 가져오기
        user_input = int(input(f"1~{count} 사이의 번호를 입력하세요. (종료는 0): "))  # 프로그램 개수 출력
        if user_input == 0:
            print("프로그램을 종료합니다.")
            break
        example.show_all_program()  # 프로그램 목록 출력
        example.call_method(f"program_{user_input}")  # 동적 메서드 호출
    except ValueError:
        print("숫자를 입력하세요.")

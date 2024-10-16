def draw(n):
    import time
    
    for b in range(4):
        print('●' if n& (1<<b) !=0 else '○',end='')
    time.sleep(0.5)
    print()               

class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1 [수열의 합]",
            "프로그램 2 [조건에 맞는 수 검색]",
            "프로그램 3 [LED 깜빡이]",
            "프로그램 4 [수식 계산]",
            "프로그램 5 [수식 그래프로 그리기]"
        ]
        
    def program_1(self, iterations = 10):
        print()
        sum = 0
        an_1 = 0
        
        for n in range(1, iterations+1):
            an = 2 * an_1 + 1
            sum += an
            an_1 = an
            print(f'a_{n} : {an}')
        print(f'총합 : {sum}')        
        
    def program_2(self):
        print()
        print("조건 : A x B^2 + C x D^2 = A x B x C x D (ABCD가 0, 1인 경우는 제외)")
        for ABCD in range(2, 10000):
            AB = ABCD // 100
            CD = ABCD % 100
            if (ABCD == AB ** 2+ CD ** 2):
                print(ABCD)
        
    def program_3(self):
        import time  
        
        print()        
        m = 1
        while True:
            for _ in range(3):
                m <<= 1
                draw(m)
            for _ in range(3):
                m >>= 1
                draw(m)                            
    
    def program_4(self):
        print()
        import math
        
        C, H = 0.7, 65
        
        data = input('Type comma seperated values:').split(',')
        D = []
        
        for d in data:
            D.append(float(d))
            
        Q = []
        for d in D:
            q = math.sqrt(2 * C  * d / H)
            Q.append(q)
            print(f'Q={q:.4f} at D={d:.4f}')
        
    def program_5(self):
        print()
        
        import matplotlib.pyplot as plt
        
        X = [x/10 for x in range(41)] # 0.1 간격으로 list 생성
        Y = []
        for x in X:
            y = x**3 - 3*x**2 - 7
            Y.append(y)
            print(f'f({X}) = {y:.3f}')
        
        plt.plot(X,Y)
        plt.grid()
        plt.show()                
    
    def call_method(self, methodName):
        if methodName.startswith('program'):            
            try:
                num = int(methodName.split("_")[1])
                if 1 <= num <= len(self.programs):
                    print()
                    self.show_program(num)
                    method = getattr(self, methodName, None)
                    if method:
                        method()
                    else:
                        print(f'Error: program_{num} 메서드가 정의되지 않았습니다.')
                else:
                    print(f"유효하지 않은 프로그램 번호입니다. : {num}")                    
            except (IndexError, ValueError):
                print(f"문자열 형식이 올바르지 않습니다. {methodName}")
        else:
            print(f"유효하지 않은 메서드 이름입니다.: {methodName}")                
                    
    def get_program_count(self):
        return len(self.programs)
    
    def show_all_program(self):
        for program in self.programs:
            print(program)
            
    def show_program(self, number):
        if 1 <= number <= self.get_program_count():
            print(self.programs[number - 1])
        else:
            print(f'유효하지 않은 번호입니다. 1에서 {self.get_program_count()} 사이의 값이어야 합니다.')
            
            
example = ExampleClass()

while True:
    try:     
        print()
        print("===============================")   
        example.show_all_program()
        print()
        userInput = input(f'1 ~ {example.get_program_count()} 사이의 수를 입력하세요(종료하려면 0을 입력하세요):')
        if userInput == '0':
            print("==== 프로그램 종료 ====")
            break
        example.call_method(f'program_{userInput}')
    except ValueError:
        print("숫자를 입력하세요.")
    
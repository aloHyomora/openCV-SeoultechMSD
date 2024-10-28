
class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1: [수식 입력, 출력]",
            "프로그램 2: [대문자, 소문자의 수 세기]",
            "프로그램 3: [두 리스트 결합]",
            "프로그램 4: [3차원 벡터 합치기]",                     
        ]            
    def program_1(self):
        print("***[프로그램 1]***")
        
        while True:
            eq=input("Eq:")
            if eq=='exit':
                break
            process(parseEquation(eq))

    
    def program_2(self):
        print("***[프로그램 2]***")
        
    
        
    def program_3(self):
        print("***[프로그램 3]***")        
        
        
    
    def program_4(self):
        print("***[프로그램 4]***")           

    
        
    def get_program_count(self):
        return len(self.programs)
        
    def show_all_programs(self):
        for i in range(self.get_program_count()):
            print(self.programs[i])
        
    def show_program(self, index):
        print(self.programs[index - 1])
        
    def call_method(self,  methodName):
        if methodName.startswith("program"):
            try:
                num = int(methodName.split('_')[1])
                if 1<= num <= self.get_program_count():
                    print()
                    self.show_program(num)
                    method = getattr(self, methodName, None)
                    if method:
                        method()
                    else:
                        print(f'에러: 메소드 이름 정의')                
                else:
                    print(f'인덱스 범위를 벗어났습니다.')                    
            except:
                print(f"유효한 문자열 형식 program_[index], 당신이 입력한 값: {methodName}")
        else:
            print('method가 program으로 시작하지 않습니다.')
                                

example = ExampleClass()

def add(a,b):
        return a+b
def sub(a,b):
        return a-b
def mul(a,b):
        return a*b
def div(a,b):
        return a/b
def pow(a,b):
        return a**b
def parseEquation(eq):
        pos = 0
        for i, c in enumerate(eq):
            if c in ['+','-','*','/','^']:
                pos, op = i,c
                break
        return float(eq[:pos].strip()),float(eq[pos+1:].strip()),op
def process(tup):
        res = funs[tup[2]](tup[0],tup[1])
        print(f'{tup[0]} {tup[2]} {tup[1]} = {res}')
funs ={'+':add, '-':sub, '*':mul, '/':div, '^':pow}

while True:
    
    print("======================================")
    example.show_all_programs()
    print("======================================")
    try:
        exampleIndex = int(input(f'1~{example.get_program_count()} 사이의 번호를 입력하세요. (종료는 0)'))
        if exampleIndex == 0: break
    except ValueError:
        print("숫자를 입력하세요.")        
    print("======================================")
    example.call_method(f'program_{exampleIndex}')
    
    
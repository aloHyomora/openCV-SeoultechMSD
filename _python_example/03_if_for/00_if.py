
class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1 [메뉴 주문]",
            "프로그램 2 [[turtle] 숫자 맞추기 게임]"            
        ]
        
    def program_1(self):
        selectedMenu = '마른안주'
        menu = {'소주':5000, '맥주':5000, '마른안주':14000,'샐러드':8000}
        
        total = menu.get(selectedMenu, -1)
        if total == -1:
            print(f"{selectedMenu}는 메뉴에 없습니다~")
        else:
            print(f"{selectedMenu} 가격은 {total}입니다.")
        
    def program_2(self):
        import turtle
        import random as rnd
        import time
        screen = turtle.Screen()
        screen.setup(500, 500)
        
        turtle1 = turtle.Turtle()
        randomValue = rnd.randint(0, 101)
        trialNum = 0 # 시도 횟수
        
        while True:
            try:
                trialNum += 1
                userInput2 = screen.textinput("입력창" ,"0 ~ 100 사의 값을 입력하세요.") 
                inputValue = int(userInput2)
                
                screen.clear()
                turtle1.write(f"{trialNum}회 시도", font=("맑은 고딕", 24, 'bold'))
                
                if inputValue > randomValue:
                    turtle1.write('작음', font=("맑은 고딕", 32, 'bold'))
                elif inputValue < randomValue:
                    turtle1.write('큼', font=("맑은 고딕", 32, 'bold'))
                else:
                    turtle1.write('축하합니다. \n 정답입니다~~~', font=("맑은 고딕", 32, 'bold'))
                    break                        
            except ValueError:
                print(f"잘못된 입력 : {userInput2}")
        screen.exitonclick()

            
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
    
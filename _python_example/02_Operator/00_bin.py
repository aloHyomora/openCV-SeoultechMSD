class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1. [2진수를 input으로 받아 10진수와 16진수 출력]",
            "프로그램 2: 파이썬에서 리스트를 어떻게 초기화합니까?",
            "프로그램 3: 클래스와 객체의 차이를 설명하시오.",
            "프로그램 4: 리스트와 튜플의 차이는 무엇인가?",
            "프로그램 5: 파이썬에서 예외 처리를 어떻게 합니까?",
            "프로그램 6: 상속이란 무엇이며, 어떻게 사용합니까?"
        ]
    
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
    
    def program_1(self):
        print("프로그램 1~")
    
    def program_2(self):
        print("프로그램 2~")
    
    def program_3(self):
        print("프로그램 3~")
    
    def program_4(self):
        print("프로그램 4~")
    
    def program_5(self):
        print("프로그램 5~")
        
    def program_6(self):
        print("프로그램 6~")

# 클래스 인스턴스 생성
example = ExampleClass()

while True:
    try:
        count = example.get_program_count()  # 프로그램 개수 가져오기
        user_input = int(input(f"1~{count} 사이의 번호를 입력하세요. (종료는 0): "))  # 프로그램 개수 출력
        example.show_all_program()  # 프로그램 목록 출력
        if user_input == 0:
            print("프로그램을 종료합니다.")
            break
        example.call_method(f"program_{user_input}")  # 동적 메서드 호출
    except ValueError:
        print("숫자를 입력하세요.")

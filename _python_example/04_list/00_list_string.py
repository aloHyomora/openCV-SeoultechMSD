
class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1: 콤마로 구분된 수 입력받아 리스트로 출력",
            "프로그램 2: 문자열 입력받아 역순 문자열로 출력",
            "프로그램 3: 공백 문자로 구분된 단어 입력받아 중복 없애고 정렬하고 공백 문자로 구분된 문자열로 출력",
            "프로그램 4: 아트배쉬(Atbash) 암호법"
        ]
    
    def program_1(self):
        strValue = input('숫자를 콤마로 구분해서 입력하세요:').split(',')
        num_list = []
        
        for s in strValue:
            num_list.append(float(s))
            
        print(num_list)
        print("======= 다른 방법 =======")
        print([float(s) for s in strValue]) # [] 괄호 주의
    
    def program_2(self):
        print()
        strValue2 = input('문자열 입력하세요:')
        length = len(strValue2)
        str_rev =''
        for i in range(length):
            str_rev += strValue2[length - i - 1]
        print(str_rev)
        print('======== 다른 방법 ========')
        str_rev = ''
        for c in strValue2:
            str_rev = c + str_rev
        print(str_rev)
        print('======== 다른 방법 ========')
        print(strValue2[::-1]) # 문자열 슬라이싱

    def program_3(self):
        print()
        strs = input('여러 단어를 입력하세요. (중복 가능):').split()
        strs = list(set(strs)) # set 중복 없애는 함수, 집합 자료형
        strs.sort()
        res = ' '.join(strs)
        print(res)
        
    def program_4(self):
        print()
        inputValue = input('암호를 입력하세요:')
        rev_value = ''
        for c in inputValue:
            if c.isalpha():
                if c.isupper():
                    x = ord('Z') - (ord(c) - ord('A'))
                    c = chr(x)
                else:
                    x = ord('z') - (ord(c) - ord('a'))
                    c = chr(x)                                                    
            elif c.isdigit():
                x = ord('9') - (ord(c) - ord('0'))
                c = chr(x)
            rev_value += c
        print(rev_value)
    def call_method(self, methodName):
        if methodName.startswith('program'):
            try:
                num = int(methodName.split("_")[1])
                if 1 <= num <= self.get_program_count():
                    print()
                    self.show_program(num)
                    method = getattr(self, methodName, None)
                    if method:
                        method()
                    else:
                        print(f'Error: program_{num} 메서드가 정의되지 않았습니다.')
                else:
                    print(f"유효하지 않은 인덱스 범위입니다: {index}")                 
            except:
                print(f"유효한 문자열 형식 program_[index], 당신이 입력한 값: {methodName}")
        else:
            print("메소드 이름이 'program'으로 시작하지 않습니다.")                                        
    
    def get_program_count(self):
        return len(self.programs)
    
    def show_all_programs(self):
        for program in self.programs:
            print(program)
            
    def show_program(self, index):
        if 1 <= index  <= self.get_program_count():            
            print(self.programs[index - 1])
        else:
            print(f"유효하지 않은 인덱스 범위입니다: {index}")
            
            
example = ExampleClass()

while True:
    try:        
        print()
        print("=========================")
        example.show_all_programs()
        print()
        userInput = input(f'1 ~ {example.get_program_count()} 사이 값을 입력하세요(프로그램 종료는 0):')
        if userInput == '0':
            break
        example.call_method(f'program_{userInput}')
    except ValueError:
        print("숫자를 입력하세요.")
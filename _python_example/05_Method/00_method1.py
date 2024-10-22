
class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1: [중복이 없는 리스트]",
            "프로그램 2: [임의 개수의 인수]",
            "프로그램 3: [가변 길이 키워드]",
            "프로그램 4: [문장 전체에서 단어와 그 단어가 출력되는 빈도 수 출력 (빈도수 내림차순)]",
            "프로그램 5: [디저트에 대한 영양 성분 데이터를 표로 만들기]",
            "프로그램 6: [dic 데이터 함축]",
            "프로그램 7: [dic 형식 변경]"            
        ]            
    def program_1(self):
        print("***[프로그램 1]***")
        
        value_list = input('리스트를 입력하세요. ex) 1,2,2,3,1,5,6,7 : ').split(',')
        
        print(list(set(value_list)))
        
        temp = []
        for value in value_list:
            if value not in temp:
                temp.append(value)
        print(temp)
    def program_2(self):
        print("***[프로그램 2]***")
        print("평균과 합을 반환하는...")
                
        # 가변길이 인수 키워드 def sumNave(*a): 
        value_list = [int(x) for x in input("콤마로 구분된 수를 입력하세요. :").split(',')]        
        
        mean = sum(value_list) / len(value_list)
        total = sum(value_list)
                                    
        temp = [(e-mean)**2 for e in value_list]
        import math
        std = math.sqrt(sum(temp)) / len(value_list)
        
        print(f"mean: {mean}, total: {total}, std: {std}")
    def program_3(self):
        print("***[프로그램 3]***")        
        print('몇 개의 인수를 전달할지 미리 알 수 없을 때 매개 변수에 **를 붙인다.')
        print('내부적으로 딕셔너리로 처리한다. key-value')
        print('예시: def calcPrism(**kwargs): 일 때 메서드 내에선 kwargs.get(\'width\', 0.0) 과 같이 사용한다.')
    
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
    
    
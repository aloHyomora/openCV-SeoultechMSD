

class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1: 'c'또는 'C'로 시작하는 모든 원소들의 집합을 구하라",
            "프로그램 2:  구두점을 제외한 모든 글자들의 개수를 출력한다. 단, 개수의 내림차순으로 정렬하여 출력한다."                     
        ]
    
    def program_1(self):
        print()
        nation = ['kr', 'En', 'Fr', 'DH', 'Kr', 'Co', 'cc', 'eu', 'to', 'cn', 'CH', 'en']
        set1 = []
        
        for language in nation:
            if language.lower().startswith('c'):
                set1.append(language)
                
        print(set(set1))
        print("====== 다른 방법 ======")
        set2 = []
        for language in nation:
            if language[0] in ['c', 'C']:
                set2.append(language)
                
        print(set2)
        
    
    def program_2(self):
        print()
        s='''"내가 다른 사람들보다 멀리 보았다면 
        그건 내가 거인의 어깨 위에 서 있었기 때문이다."-아이작 뉴튼'''
        
        alphas=list(filter(lambda x: x.isalpha(),s))

        dic=dict(zip(alphas,[0]*len(alphas)))
        for c in alphas:
            dic[c]+=1

        #c_list=sorted(dic.items(),key =lambda item:item[1],reverse=True)
        for k,v in sorted(dic.items(),key =lambda item:item[1],reverse=True):
            print(f'[{k}] : {v}')


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
                    print(f"유효하지 않은 인덱스 범위입니다: {num}")                 
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
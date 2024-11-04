import numpy as np

class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1: [0, 1로 구성된 배열로 테두리 만들기]",
            "프로그램 2: [배열 만들기]",
            "프로그램 3: [조건에 맞는 원소]",
            "프로그램 4: [1차원 배열로 만들기]",
            "프로그램 5: [디저트에 대한 영양 성분 데이터를 표로 만들기]",
            "프로그램 6: [dic 데이터 함축]",
            "프로그램 7: [dic 형식 변경]"            
        ]            
    def program_1(self):
        print("***[프로그램 1]***")
        
        arr = np.zeros((10,10), dtype=np.uint8)
        arr[:,(0,-1)] = 1 # 모든 행에서 두개의 인덱스 0, 1을 1 할당
        arr[(0,-1),:] = 1 # (0, -1) -> 첫 번째 행과 마지막 행의 모든 열에 1 할당
        # arr[:] = 1
        
        print(arr)
        
    def program_2(self):
        print("***[프로그램 2]***")
        
        print("무작위 난수 (10x10)")
        arr = np.random.randint(1,100,  (10,10))
        print(arr)
        
        print("1~100 랜덤 배치")
        arr2 = np.arange(1,101)
        np.random.shuffle(arr2)
        arr2 = arr2.reshape(10,10)
        print(arr2)
               
        print("실수 구하기 (최대, 최소)")
        arr3 = np.random.rand(10, 10)
        print(arr3)
        print(f'min: {np.min(arr3)}, max: {np.max(arr3)}')
                    
    def program_3(self):
        print("***[프로그램 3]***")        
        
        arr = np.random.randint(1, 101, size=(10,10))
        print(arr)
        A = arr[arr>=50]
        B = A[A<=60]
        
        print(B)
                
        arr2 = np.random.randint(1,10,size=(5,5))
        pos = np.where(arr2 == 5) # tuple 반환
        print(f'Array=\n {arr2}')
        print(f'index of element 5')
        for r,c in zip(pos[0],pos[1]): # tuple[0], tuple[1] -> 위치 인덱스
            print(f'({r}, {c})')
    
    def program_4(self):
        print("***[프로그램 4]***")           

        A=np.array([[[ 1,  2],
        [ 3,  4],
        [ 5,  6]],
       [[ 7,  8],
        [ 9, 10],
        [11, 12]]])
        print(A)
        B=A.flatten(order='C')
        C=A.flatten(order='F')
        print(f'C order \n {B}')
        print(f'Fortran order \n {C}')
        
    def program_5(self):
        print("***[프로그램 5]***")     

        
    def program_6(self):
        print("***[프로그램 6]***") 

    
    def program_7(self):
        print("***[프로그램 7]***")     

    
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
                print(f"예상치 못하게 프로그램이 종료되었습니다. 혹은 유효한 문자열 형식 program_[index], 당신이 입력한 값: {methodName}")
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
    
    
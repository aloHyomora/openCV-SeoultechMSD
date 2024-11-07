class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1 [회색조 그라데이션 이미지]",
            "프로그램 2 [이미지에 사각형 그리기]",
            "프로그램 3 [칼라 이미지]"           
        ]
        
    def program_1(self):
        print("[프로그램 1]")
        import cv2  #이미지 처리 라이브러리 opencv 사용
        import numpy as np
        
        L = [[v for v in range(256)] for _ in range(256)] 
        img = np.array(L, dtype=np.uint8)
        cv2.imshow('img', img)          # 이미지 표시
        cv2.waitKey(0)                  # 키 입력을 기다림
        cv2.destroyAllWindows()         # 모든 창을 닫음
        
    def program_2(self):
        print("[프로그램 2]")
        import cv2
        import numpy as np
        
        img1 = np.ones((256, 256), dtype=np.uint8) * 128
        img1[50:205,50:205] = 255
        cv2.imshow('img1',img1)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
            
    def program_3(self):
        print("[프로그램 3]")
        import cv2
        import numpy as np
        
        b,g,r = 255,128,50
        L = [[[v,g,r] for v in range(256)] for _ in range(256) ]
        img = np.array(L, dtype=np.uint8)
        img[50:205,50:205] = [0,128,255]
        cv2.imshow('img', img)          # 이미지 표시
        cv2.waitKey(0)                  # 키 입력을 기다림
        cv2.destroyAllWindows()         # 모든 창을 닫음
            
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
    
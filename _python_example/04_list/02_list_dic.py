
class ExampleClass:
    def __init__(self):
        self.programs = [
            "프로그램 1: [트럼프 카드 뽑기]",
            "프로그램 2: [최대값의 리스트, 이차원 벡터의 최대값을 모아..]",
            "프로그램 3: [최대값의 리스트2, 근데 열 끼리의 비교]",
            "프로그램 4: [문장 전체에서 단어와 그 단어가 출력되는 빈도 수 출력 (빈도수 내림차순)]",
            "프로그램 5: [디저트에 대한 영양 성분 데이터를 표로 만들기]",
            "프로그램 6: [dic 데이터 함축]",
            "프로그램 7: [dic 형식 변경]"            
        ]
    def program_1_raw(self):
        import random as rnd
    
        print("***[프로그램 1]***")
        shapes = ['♠','◇','♡','♣']
        number = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        
        cards = []
        for i in range(len(shapes)):
            for j in range(len(number)):
                cards.append(f'{shapes[i]}_{number[j]}')
                
        print("카드 뽑기 : 5명")
        
        randNum = []
        
        while len(randNum) != 5:
            data = rnd.randint(0, 52)
            if data not in randNum:
                randNum.append(data)                
            
        for i in range(5):
            print(cards[randNum[i]])
            
    def program_1(self):
        print("***[프로그램 1]***")
        
        import random as rnd
        numbers = ['A'] + [str(n) for n in range(2, 11)] + ['J', 'Q', 'K']
        suit=['♠','◇','♡','♣']
        deck = [s+' '+n for s in suit for n in numbers] # 이중 반복문 (for 안에 for)
        
        for p in range(5): # 5번 반복
            inHand = rnd.sample(deck, 7) # deck에서 7개 랜덤 선택
            for i in inHand:
                deck.remove(i)
            print(inHand)
        
    def program_2(self):
        print("***[프로그램 2]***")
        v= [[3,7,4,5], [7,12,3,9], [22,12,33,15], [1,4,2,2,1]]
        
        print("2차원 리스트 출력***")
        for i in v:
            print(i) # 1 반복에서 [3, 7, 4, 5] 출력됨
            
        print("최댓값 출력")
        maxVal = [max(data) for data in v]
        print(maxVal)
        
    def program_3(self):
        print("***[프로그램 3]***")
        v= [[3,7,4,5], [7,12,3,9], [22,12,33,15], [1,4,2,2,1]]
        
        # *v : 리스트 v에서 []를 제거
        # zip(a, b, c)는 군집 자료형 a, b, c를 같은 순서끼리 모은 zip 자료형 반환
        data = [max(col) for col in zip(*v)]
        print(data)
        
    # 사전 함축
    def program_4_raw(self):
        # 음료와 가격을 기반으로 menu 만들기
        beverage=['사과 주스', '아메리카노', '카페라떼','밀크티','소금빵']
        price=[6000,3500,4500,4000,2000]
        
        menu = {k:v for k, v in zip(beverage, price)}
        
        # 주문이 아래와 같을 때 총 금액 출력
        order = [1, 2, 0, 1, 5]
        order_dic = {item:num for item,num in zip(beverage, order)}
        total = 0
        print("======Receipt======")
        for i, num in order_dic.items():
            if num != 0:
                sub = menu[i] * num # menu 사전에서 value 받고 개수랑 곱함.
                total += sub
                print(f' {i} ({num}  \t {sub})')
                
        print(f'총합 :{total}')

    def program_4(self):
        print("***[프로그램 4]***")
        sentence="""With our sentence examples, seeing a word within
        the context of a sentence helps you better understand it and know how to
        use it correctly. From long to short, simple to complex, this tool
        can assist you with how to use words that may have more than one meaning."""
        punct=['.',',',':',';','"',"'"]
        
        # 예시 구두점에 대해서 sentence 대체 반복, 제거
        for dot in punct:
            if dot in sentence:
                sentence = sentence.replace(dot,'')
                
        # 문장을 단어로 나누기 (공백 기준)
        pool = [word.strip() for word in sentence.split()]
        
        # 중복 단어 제거
        wordset = list(set(pool))
        
        # dic 만들기
        dic = {word:pool.count(word) for word in wordset}
        
        # 내림차순 분류 (분류 기준 key, x[1]은 튜플 중 두 번째 값인 value를 의미)
        res = sorted(dic.items(), key=lambda x:x[1], reverse=True)
        
        # 출력
        for k, v in res:
            print(f'{k}: {v:2d}')
        
    def program_5(self):
        print("***[프로그램 5]***")
        desserts= ['요거트','아이샌드', '컵케이크', '생강빵']
        contents=['칼로리', '지방', '탄수화물', '단백질']
        numbers=[[159.,6.,24.,4.], [237.,9.,37.,4.3],
	        [305.,3.7,67.,3.9], [356.,16.,49.,0.0]]            
        
        print("디저트\t\t",end="")
        for c in contents:
            print(f"{c}\t\t",end="")            
        print()
        
        for i,d in enumerate(desserts):
            print(f"{d}\t\t",end="")
            for j,c in enumerate(contents):
                print(f"{numbers[i][j]}\t\t",end="")
            print()
    def program_6(self):
        print("***[프로그램 6]***")
        desserts= ['요거트','아이샌드', '컵케이크', '생강빵']
        contents=['칼로리', '지방', '탄수화물', '단백질']
        numbers=[[159.,6.,24.,4.], [237.,9.,37.,4.3],
	        [305.,3.7,67.,3.9], [356.,16.,49.,0.0]]
        
        dic = {dessert:{ content:numbers[indexD][indexC] for indexC, content in enumerate(contents)} for indexD,dessert in enumerate(desserts)}
        print(dic)
    def program_7(self):
        print("***[프로그램 7]***")
        desserts= ['요거트','아이샌드', '컵케이크', '생강빵']
        contents=['칼로리', '지방', '탄수화물', '단백질']
        numbers=[[159.,6.,24.,4.], [237.,9.,37.,4.3],
	        [305.,3.7,67.,3.9], [356.,16.,49.,0.0]]
        
        table = {(dessert,content):numbers[indexD][indexC] for indexC,content in enumerate(contents) for indexD,dessert in enumerate(desserts)}
        print(table)
        print()
        print(table[('컵케이크','지방')])
        
        
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
    
    
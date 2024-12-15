# 리스트 v의 각 원소도 리스트이다. 각 원소의 최대값을 모은 리스트 maxVal을 구하는 코드를 작성하라.
v= [[3,7,4,5], [7,12,3,9], [22,12,33,15], [1,4,2,2,1]]
maxVal = [max(lista) for lista in v]
print(maxVal)
    
maxval2 = []
print([max(col) for col in zip(*v)]) # *v 언패킹 2차원 배열을 1차원 배열 형태로 반환, zip은 각 리스트의 동일 인덱스의 요소를 묶어 튜플 생성

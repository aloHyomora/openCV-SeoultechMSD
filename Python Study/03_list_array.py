# 문자열을 입력받아 역순의 문자열을 만들고 출력하는 프로그램을 작성하라.
strs=input('Type a string:')
str_rev=''
for c in strs:
   str_rev=c+str_rev 
print(str_rev)

strs=input('Type a string:')
print(strs[::-1])      # 문자열 슬라이싱

# 800에서 1200까지의 정수 중 7의 배수이지만 5의 배수가 아닌 수들을 모두 찾아 리스트에 담는 프로그램을 작성하라.
NumList = []
for num in range(800,1201):
    if num % 7 == 0 and num % 5 != 0:
        NumList.append(num)
print(NumList)

# 콤마로 구분된 수 들을 input으로 입력받아 그 수가 포함된 리스트를 만들어 출력하는 프로그램을 만들어보자.
strs = input('Type comma separated values:').split(',')
nums = []
for s in strs:
    nums.append(s)
print(nums)

# one line
print([float(s) for s in input('Type comma seperated values:').split(',')]) #함축

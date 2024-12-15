for i in range(800, 1201):
    if i % 7 == 0 and i % 5 != 0:
        print(i)
        
n = input('콤마로 구분된 수를 입력')
nums = n.split(',')
print(nums)

print([float(s) for s in input('comma').split(',')])
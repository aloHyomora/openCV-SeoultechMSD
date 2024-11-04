import numpy as np

# n x 1 배열을 m x n 배열로 재구성하기
arr = np.arange(12)
print(arr)
reshaped_arr = arr.reshape(3,4)
print(reshaped_arr)

# 가로, 세로로 배열 합치기
A = np.arange(1,10).reshape(3,3)
B = np.eye(3,3,1)
print(A)
print(B)
print('==== np.hstack, vstack ====')
print(f'hstack A,B=\n {np.hstack((A,B))}')
print(f'vstack A,B=\n {np.vstack((A,B))}')

print('==== np.concatenate (Axis 방향으로 붙이기)====')
print(np.concatenate((A,B),axis=0))
print(np.concatenate((A,B),axis=1))

print('==== np.block ====')
print(np.block([A,B]))

# 배열 n개 배열로 나누기
arr2= np.array([[1,2,3,4,5,6,7,8]])
split_arr = np.hsplit(arr2,2)
print(split_arr)

# 3x3 배열에 랜덤한 값 생성
rand_arr = np.random.rand(3,3)
print(rand_arr)

# 지정된 간격으로 숫자 배열 생성
arr3 = np.arange(0, 10, 2)
arr4 = np.linspace(0,1,5)
print(arr3)
print(arr4)

# 합, 평균, 표준편차, 분산
arr5 = np.array([[1,2,3],[4,5,6]])
print(np.sum(arr5))
print(np.mean(arr5))
print(np.std(arr5))
print(np.var(arr5))

# 행렬 곱
arr6 = np.array([[1,2],[3,4]])
arr7 = np.array([[5,6],[7,8]])

multipliedValue = np.dot(arr6,arr7)
print(multipliedValue)

# 조건 만족 인덱스 반환
arr8 = np.array([1,2,3,4,5])
print(np.where(arr8 > 3))
print(np.where(arr8 > 3, 1, 0)) #np.where(조건, 참일 때 값, 거짓일 때 값)
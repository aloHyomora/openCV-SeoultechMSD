# 1. 3x3 크기의 NumPy 배열을 생성하고 모든 값을 1로 초기화한 뒤, 대각선의 값을 각각 10, 20, 30으로 변경하세요.
# 힌트: np.ones와 np.fill_diagonal을 사용하세요.
import numpy as np
arr = np.ones([3,3])
np.fill_diagonal(arr, [10,20,30])
print(arr)

# 2. -10부터 10까지의 값을 가지는 1차원 배열을 생성하고, 0보다 큰 값들만 필터링하여 새로운 배열로 만드세요.
# 힌트: 논리 인덱싱을 사용하세요.
import numpy as np
arr1 = np.arange(-10,11)
print(arr1)
arr2 = arr1[arr1>0]
print(arr2)

# 3. 1에서 100 사이의 랜덤 정수를 가지는 5x5 배열을 생성하고 각 행의 평균과 표준편차를 계산하세요.
# 힌트: np.random.randint와 통계 메서드의 axis 매개변수를 활용하세요.
import random as rnd
import numpy as np
arr3 = np.random.randint(1,101,size=(5,5))
row_means = np.mean(arr3, axis=1)
row_stds = np.std(arr3, axis=1)

print(f'5x5 랜덤 배열:\n',arr3)
print(f'각 행의 평균:', row_means)
print(f'각 행의 표준편차:',row_stds)

# 4. 4x4 단위 행렬(identity matrix)을 생성하고, 랜덤한 4x4 행렬과 곱하여 결과를 검증하세요.
# 힌트: np.identity와 행렬 곱셈 연산자 @를 사용하세요.
import numpy as np
import random as rnd
identity_matrix = np.identity(4) 
random_matrix = np.random.randint(1,11, size=(4,4))

result_matrix = identity_matrix @ random_matrix
print(f'4x4 단위 행렬:\n', identity_matrix)
print(f'\n4x4 랜덤 행렬:\n',random_matrix)
print(f'\n단위 행렬과 랜덤 행렬의 곲:\n',result_matrix)

# 5. 크기가 12인 1차원 배열을 생성한 후, 이를 (2, 3, 2) 형태의 3D 배열로 재구성하세요.
# 힌트: np.arange와 .reshape를 사용하세요.
import numpy as np
arr4 = np.arange(12)
arr5 = np.reshape(arr4, (2,3,2)) # arr4.reshape(2,3,2)
print(arr4)
print(arr5)

# 6. 6x6 크기의 랜덤 값 배열을 생성하고 모든 값을 0과 1 사이로 정규화(normalize)하세요.
# 힌트: (array - min) / (max - min)을 사용하세요.
import numpy as np
import random as rnd
arr6 = np.random.randint(0,101, size=(6,6))
# 정규화
min_val = np.min(arr6)
max_val = np.max(arr6)
normalized_array = (arr6 - min_val) / (max_val-min_val)

print("원본 배열\n",arr6)
print("정규화된 배열\n",normalized_array)

# 7. 값이 [1, 2, 3]인 두 개의 1차원 배열을 수직 및 수평으로 결합하세요.
# 힌트: np.vstack와 np.hstack을 사용하세요.
arr7 =  np.array([1,2,3])
arr8 = np.array([1,2,3])
arr9 = np.vstack((arr7,arr8))
arr10 = np.hstack((arr7,arr8))
print(arr9)
print(arr10)

# 8. 대각선 요소가 [4, 5, 6]인 대각행렬을 생성한 뒤, 다시 대각선 값을 추출하여 1차원 배열로 만드세요.
# 힌트: np.diag를 사용하세요.
import numpy as np
digonal_matrix = np.diag([4,5,6])
print(digonal_matrix)

diagnal_values = np.diag(digonal_matrix)
print(diagnal_values)

# 9. 연립방정식 풀기 3x+y=9, x+2y=8
import numpy as np
# 계수 행렬 (A)와 상수 벡터 (B) 정의
A = np.array([[3, 1],  # 3x + y
              [1, 2]]) # x + 2y
B = np.array([9, 8])   # 우변 값

# 연립방정식 해 풀기
solution = np.linalg.solve(A, B)

# 결과 출력
print("해결된 값 (x, y):", solution)

# 10. 3x3 배열을 생성하고 값이 5보다 큰 요소를 True, 나머지를 False로 나타내는 불리언 마스크를 만드세요.
# 힌트: 비교 연산자를 사용하세요.
import numpy as np
import random as rnd
ar1 = np.random.randint(1,10,size=[3,3])
ar2 = ar1 > 5
print(ar1)
print(ar2)

# 11. 10x10 크기의 랜덤 실수 배열을 생성하고 각 열의 모든 요소 합계를 계산하세요.
# 힌트: np.sum과 axis를 사용하세요.
import numpy as np
import random as rnd
ar3 = np.random.randint(0,11, size=[10,10])
print(ar3)
print(np.sum(ar3, axis=0))
print(np.sum(ar3, axis=1))

# 12. 5x5 배열을 생성한 후, 이를 수평 및 수직으로 뒤집으세요.
# 힌트: 슬라이싱 [::-1]을 사용하세요.
import numpy as np
ar4 = np.random.randint(0,11, size=[5,5])
flipped_horizontally = ar4[:,::-1] # 좌우반전
flipped_vertically = ar4[::-1,:]
print("원본 배열:\n", ar4)
print("\n수평으로 뒤집은 배열:\n", flipped_horizontally)
print("\n수직으로 뒤집은 배열:\n", flipped_vertically)

# 13. 랜덤 정수를 가지는 1차원 배열을 내림차순으로 정렬하고, 정렬된 요소의 원래 인덱스를 출력하세요.
# 힌트: np.argsort를 사용하세요.
import numpy as np
import random as rnd
ar5 = np.random.randint(0,51,size=10)
# 내림차순정리
sorted_indices = np.argsort(-ar5)
sorted_arr = ar5[sorted_indices]
print(ar5)
print(sorted_arr)

# 14. 3x3 배열을 생성한 후, 이를 0으로 패딩하여 최종 배열 크기가 5x5가 되도록 만드세요.
# 힌트: np.pad를 사용하세요.
ar6 = np.arange(1,10).reshape(3,3)
padded_arr = np.pad(ar6, pad_width=1, mode='constant', constant_values=0)
# 결과 출력
print("원본 배열:\n", ar6)
print("\n0으로 패딩된 배열:\n", padded_arr)

# 15. (4, 3, 2) 크기의 3D 배열을 생성하고 축을 변경하여 배열의 형태를 (3, 2, 4)로 변환하세요.
# 힌트: np.transpose를 사용하세요.
ar7 = np.arange(24).reshape(3,2,4)
transposed_arr = np.transpose(ar7, axes=(1,2,0))
print(ar7)
print(transposed_arr)
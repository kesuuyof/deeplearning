import numpy as np
# 1次元配列を作成
A = np.array([1, 2, 3, 4])
print(A)
# 配列の次元数を返す
np.ndim(A)
A.shape
A.shape[0]

# “2次元の配列を作成
B = np.array([[1,2], [3,4], [5,6]])
print(B)
np.ndim(B)
B.shape

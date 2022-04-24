import numpy as np

a = np.array([1,2,3])

# 객체의 형태
print(a.shape)

# 객체의 차원
print(a.ndim)

# 객체 내부 자료형
print(a.dtype)

# 객체 내부 자료형이 차지하는 메모리 크기
print(a.itemsize)

# 객체 전체 크기
print(a.size)

print("=====================================")

b = np.array(range(1, 11)) + np.array(range(10, 101, 10))

print(b)

print(b.shape)

print(b.size)
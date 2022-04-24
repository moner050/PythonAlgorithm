import numpy as np

array_a = np.array([0,1,2,3,4,5,6,7,8,9])
array_b = np.array(range(0, 10))
array_c = np.array(range(0, 10, 2))

print("array_a : ", array_a)
print("array_b : ", array_b)
print("array_c : ", array_c)

print("array_c 의 shape : ", array_c.shape)
print("array_c 의 ndim : ", array_c.ndim)
print("array_c 의 ctype : ", array_c.dtype)
print("array_c 의 size : ", array_c.size)
print("array_c 의 itemsize : ", array_c.itemsize)

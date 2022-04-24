import numpy as np

arr = np.full(25,0).reshape(5, 5)
arr[0:5:2, 0:5:2] = 1
arr[1:5:2, 1:5:2] = 1

print(arr)

print(arr[0].sum())
import numpy as np

a = np.arange(0, 32).reshape(4, 4, 2)
a2 = a.flatten();

# print(a)

print("10번째 원소 : ", a2[9])
print("20번째 원소 : ",a2[19])
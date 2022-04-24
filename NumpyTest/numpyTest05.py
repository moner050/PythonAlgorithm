import numpy as np

scores = np.array([88, 72, 93, 94, 89, 78, 99])

print(scores[2])
print(scores[-1])
print(scores[1:4])
print(scores[3:])

print("===========================")

ages = np.array([18, 19, 25, 30, 28])

y = ages > 20
print(y)

print(ages[ages>20])
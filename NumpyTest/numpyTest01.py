import numpy as np

mid_scores = np.array([10, 20, 30])
final_scores = np.array([60, 70, 80])

total = mid_scores + final_scores

print("시험 성적의 합계 : ", total)
print("시험 성적의 평균 : ", total/2)

print("=====================================")
a = np.array(range(1,11))
b = np.array(range(10, 101, 10))

print(a + b)
print(a - b)
print(a * b)
print(a / b)

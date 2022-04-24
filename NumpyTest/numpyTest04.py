import numpy as np

salary = np.array([220, 250, 230])

salary = salary + 100
print(salary)

salary = salary * 2
print(salary)
print("=========================")

height = np.array([1.83, 1.76, 1.69, 1.86, 1.77, 1.73])
weight = np.array([86, 74, 59, 95, 80, 68])

BMI = weight / (height**2)

print("대상자들의 BMI : \n", BMI)
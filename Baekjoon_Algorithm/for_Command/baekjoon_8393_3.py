"""
    n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

    첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

    1부터 n까지 합을 출력한다.
"""

n = int(input())
plus = 0

if n <= 10000 and n >= 1 :
    for i in range(n+1) :
        plus += i
    print(plus)
else :
    print("입력할수있는 n의 값의 범위를 초과했습니다.")
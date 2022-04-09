"""
    N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

    첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다.
    모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

    첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
"""

N = int(input())

if N >= 1 and N <= 1000000 :

    num = list(map(int, input().split()))

    min = num[0]
    max = num[0]

    for i in num[1 : ] :
        if i > max :
            max = i
        elif i < min :
            min = i

    print(min, max)
else :
    print("N의 값이 범위를 벗어났습니다.")

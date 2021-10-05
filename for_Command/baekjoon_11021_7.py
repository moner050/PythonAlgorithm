"""
    두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
    첫째 줄에 테스트 케이스의 개수 T가 주어진다.
    각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
    각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.


"""
T = int(input())

for i in range(1,T+1) :
    A,B = map(int, input().split())
    plus = A + B
    if A > 0 and B < 10 :
        print("Case #%d: %d" % (i,plus))
    else :
        print("A 또는 B의 값이 범위를 벗어났습니다.")
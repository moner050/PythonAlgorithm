# 두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

A,B = map(int, input().split())

plusResult = A + B
minusResult = A - B
multiplicationResult = A * B
devideResult = A // B
restResult = A % B

print(plusResult)
print(minusResult)
print(multiplicationResult)
print(devideResult)
print(restResult)
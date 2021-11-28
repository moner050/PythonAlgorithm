'''
    알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오.
    단, 대문자와 소문자를 구분하지 않는다.
    첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
    첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.
'''

# 입력된 값을 모두 소문자로 변경
word = input().lower()
# 입력된 문자열의 중복을 제거 후 리스트로 변형.
word_list = list(set(word))
cnt = []

for i in word_list :
    # 입력된 문자열이 얼마나 있나 카운트
    count = word.count(i)
    cnt.append(count)

if cnt.count(max(cnt)) >= 2 :
    print('?')
else :
    print(word_list[(cnt.index(max(cnt)))].upper())
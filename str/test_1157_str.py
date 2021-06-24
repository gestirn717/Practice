# 문제
# 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 
# 단, 대문자와 소문자를 구분하지 않는다.

# 입력
# 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.

# 출력
# 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


# 1.문자 대문자로 바꾸서 입력받기
# 2.단어를 리스트로 만들어서 각 문자별로 분리시켜
# 3.리스트를 만들고 각 문자별로 나온횟수 리스트로 저장
# 4.횟수는 아스키코드 숫자 이용 
# 5.문자는 chr로 받음

w = input().upper()

lst = list(w)
# print(lst)
a = []
for i in range(ord("A"),ord("Z")+1):

    a.append(lst.count(chr(i)))
     
b = max(a)

if a.count(b) == 1:
    print(chr(a.index(b)+ord("A")))
else:
    print("?")

# w = list(input().upper())

# a = []
# for  i in range(ord("A"),ord("Z")+1):
#     a.append(w.count(chr(i)))

# b = max(a)

# if a.count(b) == 1:
#     print(chr(a.index(b)+ord("A")))
# else:
#     print("?")

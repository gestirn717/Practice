# 문제
# 그룹 단어란 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우만을 말한다. 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.

# 단어 N개를 입력으로 받아 그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 단어의 개수 N이 들어온다. N은 100보다 작거나 같은 자연수이다. 둘째 줄부터 N개의 줄에 단어가 들어온다. 단어는 알파벳 소문자로만 되어있고 중복되지 않으며, 길이는 최대 100이다.

# 출력
# 첫째 줄에 그룹 단어의 개수를 출력한다.

# 예제 입력 
# 3
# happy
# new
# year

# 예제 출력 
# 3

# 예제 입력 
# 4
# aba
# abab
# abcabc
# a

# 예제 출력
# 1

# 1. 테스트케이스 횟수 입력받기
# 2. 그룹단어 갯수 카운터
# 3. for문 (횟수) 돌리기
# 4. 문자 입력받기
# 5. 리스트 만들기
# 6. for문 - 입력받은 문자열의 길이 
# 7. 리스트안에 문자열의 인덱스(문자)가 없으면 리스트에 추가
# 8. 리스트 마지막 문자와 입력받은 문자가 같으면 컨티뉴 

# t = int(input()) #테스트케이스
# count = 0 #그룹단어 갯수 카운터

# for i in range(t):

#     s = input(); #문자열입력
#     arr = []

#     flag = 1
#     for i in range(len(s)):
#         if s[i] not in arr:
#             arr.append(s[i])
#         else:
#             #체크해야함...
#             if arr[-1] == s[i]: #같은 문자가 연속되므로 continue
#                 continue;
#             else: #새로운 문자
#                 flag = 0
#                 break;

#     if flag == 1:
#         count += 1

# print(count)



# 1. 테스트케이스 횟수 입력받기
# 2. 그룹단어 갯수 카운터
# 
# 입력 받은 단어 앞에서부터 차례로 다음 글자와 비교 / 일치하면 pass, 다음 글자를 비교
# 모두 pass 되면 맨 마지막은 j = len(word)-1   

num = int(input())
count = 0

for i in range(num):
    word = input()

    for j in range(len(word)):
        if j != len(word)-1:

            if word[j] == word[j+1]: #다음 글자와 일치하면 패스
                pass
            elif word[j] in word[j+1: ]: #다음 글자부터 끝까지 중에 같은 글자가 나오면 멈춤
                break
        else: #멈춤없이 pass하면 카운터에 1추가
            count += 1
print(count)


# t_case = int(input())
# cnt = 0
# for i in range(t_case):
#     w = list(str(input()))
    
    
#     for j in range(len(w)):
#         if j != len(w) - 1: #마지막이 아닐때 
#             if w[j] == w[j+1]:
#                 pass
#             elif w[j] in w[j+1: ]:
#                 break


#         else:
#             cnt += 1
# print(cnt)
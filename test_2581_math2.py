# 문제
# 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.

# 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.

# 입력
# 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다.

# M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.

# 출력
# M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 

# 단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

# 예제 입력 
# 60
# 100

# 예제 출력 
# 620
# 61

# 예제 입력 
# 64
# 65
# 예제 출력 
# -1


import sys

m = int(sys.stdin.readline())
n = int(sys.stdin.readline())
a_lst = []

#2를 제외한 2의 배수 모두 제외
for i in range(m, n+ 1):
    if i >1 and (i==2 or i%2 !=0):
        a_lst.append(i)

cnt = len(a_lst)
s = sum(a_lst)
b_lst = []



# i는 a_lst에 포함된 숫자
# j는 i-1 까지의 숫자 
# i % j가 0이 된다면 약수가 있다는 의미

for i in a_lst:
    a = 0
    for j in range(3,i,2): #홀수  
        if i%j == 0:
            s -= i
            cnt -= 1
            a += 1
            break
    if a < 1:
        b_lst.append(i)

if len(b_lst) == 0:
    print(-1)

else:
    print(s)
    print(b_lst[0])



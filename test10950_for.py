# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오

# 첫째 줄에 테스트 케이스의 개수 T가 주어진다.
# 각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

# 풀어서 쓰면  첫번째 받는 숫자는 더하기 진행할 횟수 받고 for문 돌아서 더하기 진행

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    print(a+b)
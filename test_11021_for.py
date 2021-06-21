n = int(input())
m = 0
for i in range(n):
    a, b = map(int, input().split())
    m = i+1
    print(f"Case #{m}:",a+b)
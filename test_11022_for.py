n = int(input())
m = 0
for i in range(n):
    a, b = map(int, input().split())
    m = i+1
    print("Case #%d: %d + %d = %d" %(m,a,b,a+b))
# input 대신에 sys.stdin.readline() 사용하기
# int 변환이나 slpit()사용가능
# 뱐수저장해서 쓰는것도 좋음 ex) input = sys.stdin.readline()
import sys
input = sys.stdin.readline

n = int(input())
for i in range(n):
    a,b = map(int, input().split())
    print(a+b)


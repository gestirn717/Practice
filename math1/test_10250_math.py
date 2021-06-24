

# 입력 t 개의 테스트 케이스
# h = 층수 / w = 층당 객실 갯수 / n = 손님번호 
# 손님은 아래층, 1호라인에 가까운걸 선호


# 1. for 문 안에서 실행
# 2. 각 정보들 입력받아
# 3. 카운터 넣고 이중 포문  (1호에서 높이만 변하고 2호에서 높이만 변하고)
# 4. if 문으로 카운터가 입력받은 호실 될때까지 +1 실행하도록 



T = int(input())

for i in range(T):
    H,W,N = map(int,input().split())
   
    room = 0
    for w in range(1,W+1):
        for h in range(1,H+1):
            room += 1
            if room == N:
                print(h*100 + w)






T = 10
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    count = int(input())
    bd = list(map(int, input().split()))
    lb = len(bd)
    prospect = 0
    for b in range(2,lb-5+1):
        f = b - 1
        ff = b - 2
        t = b + 1
        tt = b + 2
        maxh = max(bd[f],bd[ff],bd[t],bd[tt]) # 4개 빌딩들 중 가장 높은 것
        if bd[b] > maxh:
            prospect += bd[b] - maxh
    
    print(f'#{test_case}',prospect)
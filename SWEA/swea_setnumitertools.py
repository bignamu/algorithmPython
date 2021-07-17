
from itertools import combinations

T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())   
    cnt = 0
    A = [i for i in range(1,13)]
    c = list(combinations(A,N))
    for cc in c:
        
        if sum(cc) == K:
            print(cc)
            cnt += 1

    print(f"#{test_case}",cnt)
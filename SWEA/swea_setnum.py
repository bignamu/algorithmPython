
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())   
    cnt = 0

    for i in range(1<<N):
        temp = []
        for j in range(N):
            if i&(1<<j):
                temp.append(i)
        
        if sum(temp) == K:
            cnt += 1

    print(f"#{test_case}",cnt)
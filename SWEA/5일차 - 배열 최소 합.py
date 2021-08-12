from collections import deque

def per(k,midV):

    global minV
    
    if minV < midV:
        return
    if k == N:
        if minV > midV:
            minV = midV
    for i in range(N):

        if not visited[i]:
            visited[i] = True
            per(k+1,midV + BRD[k][i])
            visited[i] = False
        

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    BRD = [list(map(int,input().split())) for _ in range(N)]
    minV = 1e10000000
    visited = [False] * N

    per(0,0)
    print(f'#{test_case}',minV)


    
''' 
3
3
2 1 2
5 8 5
7 2 2
3
9 4 7
8 6 5
5 3 7
5
5 2 1 1 9
3 3 8 3 1
9 2 8 8 6
1 5 7 8 3
5 5 4 6 8
 '''
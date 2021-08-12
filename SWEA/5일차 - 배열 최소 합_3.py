
        


T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    BRD = [list(map(int,input().split())) for _ in range(N)]
    minV = 1e10000000
    ans = 0
    visited = [False] * N

    def dfs(r,minn):
        global ans
        ans += minn
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                dfs(r+1)
                visited[i] = False
    dfs(0)
    print(f'#{test_case}',minV)



''' 
1
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
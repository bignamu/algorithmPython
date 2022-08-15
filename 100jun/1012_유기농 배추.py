# https://www.acmicpc.net/problem/1012


from collections import deque
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())

# start = (0,0)


def bfs(start, g):
    q = deque()
    q.append((start[0], start[1]))
    while q:
        x, y = q.popleft()
        if g[x][y] == 1:
            g[x][y] = -1
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    q.append((nx, ny))
    return 1


for _ in range(t):
    m, n, k = map(int, input().split())

    graph = [[0 for _ in range(n)] for _ in range(m)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, input().split())
        graph[x][y] = 1
    # print(graph)

    for i in range(m):
        for j in range(n):
            if graph[i][j] == 0 or graph[i][j] == -1:
                continue
            cnt += bfs((i, j), graph)
    print(cnt)

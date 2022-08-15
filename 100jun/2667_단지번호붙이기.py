# https://www.acmicpc.net/problem/2667


from collections import deque
# import sys
# input = sys.stdin.readline
n = int(input())

maps = [list(input().strip()) for _ in range(n)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = []
# start = (0,0)


def bfs(start):
    cnt = 0
    q = deque()
    # sx, sy = start
    # if maps[sx][sy] == '0' or maps[sx][sy] == '-1':
    #     return
    q.append(start)

    while q:
        x, y = q.popleft()

        if maps[x][y] == '1':
            maps[x][y] = '-1'
            cnt += 1

            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                if nx >= 0 and nx < n and ny >= 0 and ny < n and maps[nx][ny] == '1':
                    q.append((x+dx[i], y+dy[i]))

    answer.append(cnt)


def sol():
    for i in range(n):
        for j in range(n):
            if maps[i][j] == '0' or maps[i][j] == '-1':
                continue
            bfs((i, j))

    print(len(answer))
    answer.sort()
    for ans in answer:
        print(ans)

# import sys
# si = sys.stdin.readline
# def mis(): return map(int, si().split())


# if __name__ == '__main__':
#     n = int(si())
#     graph = [list(map(int, si().strip())) for _ in range(n)]
#     print(graph)
if __name__ == '__main__':
    # print(maps)

    sol()

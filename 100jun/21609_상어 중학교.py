# https://www.acmicpc.net/problem/21609

import sys

from numpy import mat

input = sys.stdin.readline

n, m = map(int, input().split())


matrix = []

visited = [[0]*n for _ in range(n)]

for _ in range(n):

    matrix.append(list(map(int, input().split())))


cnt = 0
# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def findblock(r, c, v, visited, delete=False):
    global cnt

    if (r < 0 or r >= n) or (c < 0 or c >= n):
        return

    if v != matrix[r][c] and matrix[r][c] != 0 and matrix[r][c] != -5:
        return

    if(visited[r][c] == 1):
        return

    if(matrix[r][c] == -1):
        return

    visited[r][c] = 1
    cnt += 1

    if not delete:
        for i in range(4):
            findblock(r+dx[i], c+dy[i], v, visited)

    # visited[r][c] = 0

    print(cnt)

    if delete:
        for i in range(4):
            findblock(r+dx[i], c+dy[i], v, visited, True)
        matrix[r][c] = -5


def findmax(visited):
    global cnt
    max_block = -999999
    max_block_num = (0, 0)
    for i in range(n):
        for j in range(n):
            cnt = 0
            findblock(i, j, matrix[i][j], visited)
            if cnt > max_block:
                max_block = cnt
                max_block_num = (i, j)
    return max_block_num


def grav():

    for i in range(n):

        stk = []
        for j in range(n):
            if matrix[j][i] != -5 and matrix[j][i] != -1:
                stk.append(matrix[j][i])
                matrix[j][i] = -5
            if matrix[j][i] == -1:
                go_cnt = j
                while stk:
                    go_cnt -= 1
                    matrix[go_cnt][i] = stk.pop()
            if stk and j == n-1:
                go_cnt = j
                while stk:
                    matrix[go_cnt][i] = stk.pop()
                    go_cnt -= 1


def rota():
    arr = [[0 for _ in range(n)] for _ in range(n)]
    ii = 0
    for i in range(n-1, -1, -1):

        for j in range(n):
            arr[ii][j] = matrix[j][i]

        ii += 1
    return arr


def start(matrix, visited):
    visited = [[0]*n for _ in range(n)]
    i, j = findmax(visited)

    findblock(i, j, matrix[i][j], visited, True)

    grav()
    matrix = rota()
    grav()


start(matrix, visited)
print('hi')

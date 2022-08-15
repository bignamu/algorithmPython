# https://www.acmicpc.net/problem/3190

import sys

input = sys.stdin.readline

N = int(input())
K = int(input())


maps = [[0]*N for _ in range(N)]
apple = []
drive = []

# 상우하좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for _ in range(K):
    x, y = map(int, input().split())
    maps[x-1][y-1] = 'A'
    apple.append((x-1, y-1))

L = int(input())

for _ in range(L):
    temp = input().split()
    x = int(temp[0])
    y = temp[1]
    drive.append((x, y))

# 상우하좌


def move():
    global flag
    chk_len = len(loca)
    drv_loca = []
    for loca_idx, loca_val in enumerate(drivLoca):
        x, y, d, loca_cnt = loca_val
        if loca_cnt <= 0:
            continue
        for i, v in enumerate(loca):
            vx, vy, _ = v
            if vx == x and vy == y:
                loca[i] = (vx, vy, d)
                drivLoca[loca_idx] = (x, y, d, loca_cnt-1)
                drv_loca.append(loca_idx)

    for j in range(len(loca)-1, -1, -1):
        x, y, d = loca[j]
        x = x+dx[d]
        y = y+dy[d]
        if x >= N or y >= N or x < 0 or y < 0:
            flag = 1
            break

        # if (x, y, d) in loca:
        #     flag = 1
        #     break
        for si, sv in enumerate(loca):
            sx, sy, _ = sv
            if si == j:
                continue
            if sx == x and sy == y:
                flag = 1
                break
        if maps[x][y] == 'A':
            loca.append((x, y, d))
            maps[x][y] = 0
            break
        loca[j] = (x, y, d)
    if chk_len != len(loca):
        for cl in drv_loca:
            clx, cly, cld, clcnt = drivLoca[cl]
            drivLoca[cl] = (clx, cly, cld, clcnt+1)

# print(apple, drive, maps)


t = 0

global flag

# 상우하좌
loca = [(0, 0, 1)]
drivLoca = []
while 1:
    flag = 0
    if drive:
        if t == drive[0][0]:
            turn = drive.pop(0)
            if turn[1] == 'D':
                dd = loca[-1][2]+1
                if dd == 4:
                    dd = 0
            elif turn[1] == 'L':
                dd = loca[-1][2]-1
                if dd < 0:
                    dd = 3
            drivLoca.append((loca[-1][0], loca[-1][1], dd, len(loca)))

    move()

    t += 1

    if flag:
        print(t)
        break

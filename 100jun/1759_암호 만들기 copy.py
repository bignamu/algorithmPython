# https://www.acmicpc.net/problem/1759

import sys
input = sys.stdin.readline

l, c = map(int, input().split())

_list = []
_list = list(map(str, input().split()))
_list.sort()

ismo = ['a', 'e', 'i', 'o', 'u']
used = [0]*c

# print(_list)

mo = 0
ja = 0


def recur(start, p, prev):

    if start > c:
        return
    # if used[start] == 1:
    #     return

    if sum(used) == l:
        cnt = 0
        cntmo = 0
        flag = 0
        for pp in p:
            if pp not in ismo:
                cnt += 1
            if pp in ismo and not cntmo:
                cntmo += 1

        if cnt >= 2 and cntmo >= 1:
            flag = 1
        if flag:
            print(p)
        return

    for i in range(start, c):
        # if used[i] == 1:
        #     continue
        used[i] = 1
        recur(i+1, p+_list[i], _list[i])
        used[i] = 0


recur(0, '', '')

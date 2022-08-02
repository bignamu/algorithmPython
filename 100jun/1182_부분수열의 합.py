# https://www.acmicpc.net/problem/1182

import sys
input = sys.stdin.readline

n, s = map(int, input().split())

_list = list(map(int, input().split()))

used = [0]*n


global cnt
cnt = 0


def findk(k):
    if k > n:
        return
    global cnt
    for i in range(n):
        end = i
        k_sum = 0
        flag = 0
        while(end < i+k):
            if i+k > n:
                break
            k_sum += _list[end]
            end += 1
            flag = 1
        if k_sum == s and flag == 1:
            cnt += 1

    return findk(k+1)


findk(1)
print(cnt)

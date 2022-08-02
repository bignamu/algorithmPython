# https://www.acmicpc.net/problem/1759

from itertools import permutations as per

import sys
input = sys.stdin.readline

l, c = map(int, input().split())

_list = []
_list = list(map(str, input().split()))

print(_list)

ans = []
for a in per(_list, l):
    # i = 0
    # prev = a[i]
    flag = 0
    for idx, b in enumerate(a):
        if idx == 0:
            continue
        if ord(b) < ord(a[idx-1]):
            flag = 1
            break

    if not flag:
        # print(''.join(a))
        ans.append(''.join(a))

    # i += 1
ans.sort()

for a in ans:
    print(a)

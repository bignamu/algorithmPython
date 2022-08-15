# https://www.acmicpc.net/problem/14867

import sys

input = sys.stdin.readline

a, b, c, d, = map(int, input().split())

global result
result = 200001


def sol(ia, ib, cnt, prev):
    global result

    if cnt > result:
        return

    for pa, pb in prev:
        if ia == pa and ib == pb:

            return
    if ia == c and ib == d and result > cnt:
        # print(cnt, result, prev, ia, ib, len(prev))
        result = cnt
        # if (a, 0) in prev and (0, b) in prev:
        #     result -= 2
        return

    # if a == c and b == d and cnt > result:
    #     return

    # fill
    prev.append((ia, ib))
    if ia < a:

        sol(a, ib, cnt+1, prev)

    if ib < b:
        sol(ia, b, cnt+1, prev)

    # empty
    if ia != 0:
        sol(0, ib, cnt+1, prev)

    if ib != 0:
        sol(ia, 0, cnt+1, prev)

    # move
    # a에서 b로
    if ia+ib > b and ib < b:
        sol(ia+ib-b, b, cnt+1, prev)
    elif ia+ib <= b:
        sol(0, ia+ib, cnt+1, prev)

    # b에서 a로
    if ia+ib > a and ia < a:
        sol(a, ia+ib-a, cnt+1, prev)
    elif ia+ib <= a:
        sol(ia+ib, 0, cnt+1, prev)

    prev.pop()


sol(0, 0, 0, [])
if result == 200001:
    print(-1)
else:
    print(result)

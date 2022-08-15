# https://www.acmicpc.net/problem/14867

import sys
from collections import deque

input = sys.stdin.readline

a, b, c, d, = map(int, input().split())
visited = set()
cnt = -1

# a, b, count
q = deque([(0, 0, 0)])
while q:
    qa, qb, qc = q.popleft()

    if qa == c and qb == d:
        cnt = qc
        break

    if (qa, qb) in visited:
        continue

    visited.add((qa, qb))
    # fill
    if qa < a:
        q.append((a, qb, qc+1))
    if qb < b:
        q.append((qa, b, qc+1))

    # remove
    if qa > 0:
        q.append((0, qb, qc+1))
    if qb > 0:
        q.append((qa, 0, qc+1))

    # move a에서 b로
    if not (qa == 0 and qb == 0):
        if qa+qb > b and qb < b:
            q.append((qa+qb-b, b, qc+1))
        elif qa+qb <= b:
            q.append((0, qa+qb, qc+1))
        # move b에서 a로
        if qa+qb > a and qa < a:
            q.append((a, qa+qb-a, qc+1))
        elif qa+qb <= a:
            q.append((qa+qb, 0, qc+1))


print(cnt)

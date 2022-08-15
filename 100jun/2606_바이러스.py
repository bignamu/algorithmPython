import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

t = int(input())

computer = [[] for _ in range(n+1)]
used = [0 for _ in range(n+1)]

for _ in range(t):
    a, b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

# print(computer)


def bfs(start):
    q = deque([start])
    used[start] = 1
    while q:

        qq = q.popleft()
        # if used[qq]==1:
        #     continue
        # print(q)
        for i in computer[qq]:
            if used[i] == 1:
                continue
            used[i] = 1
            q.append(i)


if __name__ == '__main__':
    bfs(1)
    print(sum(used)-1)

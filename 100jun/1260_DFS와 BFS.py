# https://www.acmicpc.net/problem/1260

from collections import deque

n, m, v = map(int, input().split())

edges = [[]for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    e1, e2 = map(int, input().split())
    edges[e1].append(e2)
    edges[e2].append(e1)
    edges[e1].sort()
    edges[e2].sort()

# print(graph)


def dfs(start):

    visited[start] = 1

    print(start, end=' ')

    for i in edges[start]:

        if visited[i] == 1:
            continue

        dfs(i)


def bfs(start):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    q = deque(edges[start])
    print()
    print(start, end=' ')
    while q:

        qq = q.popleft()
        if visited[qq] == 1:
            continue

        visited[qq] = 1
        print(qq, end=' ')

        for i in edges[qq]:
            q.append(i)


dfs(v)
bfs(v)

# https://www.acmicpc.net/problem/17616

import collections

def bfs(X, adj):
    rtn = 0
    q = collections.deque()
    q.append(X)
    visited[X] = True

    while q:
        v = q.popleft()
        for nv in adj[v]:
            if not visited[nv]:
                q.append(nv)
                visited[nv] = True
                rtn += 1

    return rtn

N, M, X = map(int, input().split())
higher_adj = [[] for _ in range(N+1)]
lower_adj = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for _ in range(M):
    A, B = map(int, input().split())
    higher_adj[A].append(B)
    lower_adj[B].append(A)

print(1+bfs(X, lower_adj), N-bfs(X, higher_adj))
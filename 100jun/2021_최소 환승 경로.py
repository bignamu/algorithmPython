# https://www.acmicpc.net/problem/2021

from collections import deque


N, L = map(int,input().split())

sub = [deque() for _ in range(L+1)]
hub = [deque() for _ in range(N+1)]
for i in range(1,L+1):
    temp = list(map(int,input().split()))
    for t in temp:
        if t == -1:
            break
        hub[t].append(i)
        sub[i].append(t)
print(hub,'\n',sub)
    
visited = [0] * (L+1)

start, end = map(int,input().split())

def bfs(start):

    q = deque([start])
    visited[start] = 1
    while q:
        v = q.popleft()
        print(v,end=' ')

        for i in sub[v]:
            if 
            if not visited[i]:
                q.append(i)
                visited[i] = 1

bfs(start)
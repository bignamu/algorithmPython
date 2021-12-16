N,M,K,X = map(int,input().split())


graph = [[] for _ in range(N+1)]
visited = [-1]*(N+1)
for _ in range(M):
    s,e = map(int,input().split())
    graph[s].append(e)
    

from collections import deque
def bfs(start):

    q = deque([start])
    visited[start] += 1
    while q:
        s = q.popleft()
        
        # print(s)
        for i in graph[s]:
            if visited[i] < 0:
                visited[i] = visited[s] + 1
                q.append(i)

bfs(X)

flag = False
if not K in visited:
    print(-1)
    flag = True

if not flag:
    for i,v in enumerate(visited):
        if v==K:
            print(i)


# print(graph)
# print(visited)
''' 
4 4 2 1
1 2
1 3
2 3
2 4
'''
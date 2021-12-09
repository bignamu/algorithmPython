N,M,K,X = map(int,input().split())

bridge = [ [] for _ in range(N+1)]
distance = [-1]*(N+1)
for _ in range(M):
    s, e = map(int,input().split())
    bridge[s].append(e)


from collections import deque
def bfs(graph,start,distance):
    
    queue = deque([start])
    distance[start] = 0
    while queue:
        
        v = queue.popleft()
        # print(v,queue)
        
        for next in graph[v]:
            if distance[next] == -1:
                distance[next] = distance[v] + 1
                queue.append(next)
        
        
                


bfs(bridge,X,distance)
# print(N,M,K,X)
# print(bridge)

# print(distance)

chk = False
for k in range(1,N+1):
    if distance[k] == K:
        print(k)
        chk = True

if not chk:
    print(-1)
''' 
4 4 2 1
1 2
1 3
2 3
2 4
'''
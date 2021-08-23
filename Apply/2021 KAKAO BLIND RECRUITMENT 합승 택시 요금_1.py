# https://programmers.co.kr/learn/courses/30/lessons/72413

from collections import deque
import heapq
import copy

def solution(n, s, a, b, fares):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [0] * (n+1)
    INF = int(1e9)
    distance = [INF] * (n+1)
    for v1,v2,ed in fares:
        graph[v1].append((ed,v2))
        graph[v2].append((ed,v1))
    
    def dijkstra(start):
        q = []

        heapq.heappush(q,(0,start))
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[0]
                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(q,(cost,i[1]))
    
    dijkstra(s)
    origin = copy.deepcopy(distance)
    minn = [distance[a]+distance[b]]
    for i in range(1,n+1):
        distance = [INF] * (n+1)
        dijkstra(i)
        minn.append(origin[i] + distance[a] + distance[b])
    
    # print(min(minn))
    answer = min(minn)
    
    return answer
    

n,	s,	a,	b = 6,	4,	6,	2
fares= [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n,s,a,b,fares)
# https://www.acmicpc.net/problem/17616

import sys
from collections import deque

n,m,x = map(int,sys.stdin.readline().split())
indegree = [0] * (n+1)
graph = [ [] for _ in range(n+1)]
for _ in range(m):
    # 작은 수에서 큰 수로
    first, last = map(int,sys.stdin.readline().split())
    graph[last].append(first)
    indegree[first] += 1

def topology_sort():
    result = []
    q = deque()
    
    for i in range(1,n+1):
        if not indegree[i]:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        
        for i in graph[now]:
            indegree[i] -= 1
            if not indegree[i]:
                q.append(i)
    # for i in result:
        # print(i)

topology_sort()

for g in graph:
    if x in g:
        where = graph.index(g)

# print('where',where)
where -= 1
length = 0
while not graph[where] and where>0:
    length += 1
    where -= 1
print(min(range(1,length+1)),max(range(length+1)))
# print(length)
# print(graph,indegree)
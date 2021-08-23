from collections import deque
import copy

def solution(n, s, a, b, fares):
    answer = 0
    graph = [deque() for _ in range(n+1)]
    visited = [0] * (n+1)
    for v1,v2,ed in fares:
        graph[v1].append((v2,ed))
        graph[v2].append((v1,ed))
    print(graph)
    

    global edge,e,ago,bgo
    edge = 10e1000000
    e = 0
    egs = []
    mincandi = []
    ago = [edge]
    bgo = [edge]
    def dfs(v):
        global edge,e,ago,bgo
        visited[v] = 1
        print('----- v : ',v)
        print(f'----e : {e}')
        sumegs = sum(egs)
        print(f'----egs : {egs},{sumegs}\n')
        if visited[a] and not visited[b]:
            if sum(egs) < sum(ago):
                ago = copy.deepcopy(egs)

        if visited[b] and not visited[a]:
            if sum(egs) < sum(bgo):
                bgo = copy.deepcopy(egs)
        
        if  sum(egs) > edge:
            print(f'edge : {edge}저장한 edgs값보다 큼 돌아가기')
            return
        
        if visited[a] + visited[b] == 2:
            if sum(egs) < edge:
                edge = sum(egs)
                mincandi.append(edge)
            print(f'a,b 방문했음 {v}에서 돌아간다')
            
            return

        for i,ed in graph[v]:
            if not visited[i]:
                egs.append(ed)
                dfs(i)
                
                visited[i] = 0
                egs.pop()

    flag = False
    dfs(s)
    if not mincandi:
        flag = True
    if not flag and len(mincandi) == 1:
        print(min(mincandi)-1)
        answer = min(mincandi)-1
    if not flag and len(mincandi) > 1:
        print(min(mincandi))
        answer = min(mincandi)
    if flag:
        print(sum(ago)+sum(bgo))
        answer = sum(ago)+sum(bgo)
    return answer
    

n,	s,	a,	b = 6,	4,	6,	2
fares= [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

solution(n,s,a,b,fares)
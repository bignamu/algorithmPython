# https://programmers.co.kr/learn/courses/30/lessons/43164

# 테케 12 실패
from collections import defaultdict


def solution(tickets):
    answer = []
    _dict = defaultdict(list)
    visited = {}
    
    for tic in tickets:
        start, end = tic
        _dict[start].append(end)
        visited[start+end] = False
        
    
    _list = list(visited.keys())

    # print(visited,_dict)
    
    def dfs(start):
        
        # print(f'!!now {start}')
        answer.append(start)
        graph = _dict[start]    
        graph.sort()
        for v in graph:
            # print(f'check {v}')
            if not visited[start+v]:
                visited[start+v] = True
                
                
                dfs(v)
    
    dfs("ICN")

    return answer


tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

print(solution(tickets))
# https://programmers.co.kr/learn/courses/30/lessons/43164

# 테케 12 실패
from collections import defaultdict
import copy


def solution(tickets):
    
    
    global _dict, visited,answer
    answer = []
    _dict = defaultdict(list)
    visited = defaultdict(int)
    
    for tic in tickets:
        start, end = tic
        _dict[start].append(end)
        visited[start+end] += 1
        
    
    visited2 = copy.deepcopy(visited)
    _dict2 = copy.deepcopy(_dict)
    print(visited,_dict)

    global previous   
    previous = "ICN"
    
    def dfs(start):
        global _dict
        global visited, answer
        if len(answer) < len(tickets)+1 and not _dict[start]:
            visited = copy.deepcopy(visited2)
            _dict = copy.deepcopy(_dict2)
            answer = []
            return

        print(f'!!now {start}')
        answer.append(start)
        graph = _dict[start]
        graph.sort()


        for v in graph:
            print(f'check {v}')
            if visited[start+v]:
                visited[start+v] -= 1
                _dict[start].remove(v)
                
                dfs(v)
    
    dfs("ICN")

    return answer


tickets = [['ICN','B'],['B','ICN'],['ICN','A'],['A','D'],['D','A']]

print(solution(tickets))
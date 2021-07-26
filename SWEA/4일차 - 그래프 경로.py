
from collections import deque


T = int(input())

for test_case in range(1, T + 1):

    
    V,E = map(int, input().split())

    visited = [0 for _ in range(V+1)]
    
    node = [[] for _ in range(V+1)]
    for _ in range(E):
        front,tail = map(int, input().split())
        node[front].append(tail)
    S, G = map(int, input().split())

    print(node,visited,V,E)

    q = []
    q.append(S)
    flag = 0
    while q:
        qq = q.pop()
        visited[qq] = 1

        for nxt in node[qq]:
            if nxt == G:
                print(f'#{test_case}',1)
                flag = 1
                break
            if node[nxt] and visited[nxt] == 0:
                q.append(nxt)
        if flag == 1:
            break
    if flag == 0:
        print(f'#{test_case}',0)

        

    
""" 
3
6 5
1 4
1 3
2 3
2 5
4 6
1 6
7 4
1 6
2 3
2 6
3 5
2 5
9 9
2 6
4 7
5 7
1 5
2 9
3 9
4 8
5 3
7 8
1 9
"""


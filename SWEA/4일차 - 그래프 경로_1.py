
T = int(input())

for test_case in range(1, T + 1):

    
    V,E = map(int, input().split())

    visited = [0 for _ in range(V)]
    stack = []
    node = []
    for i in range(E):
        start,end = map(int, input().split())
        node.append([start,end])
    S, G = map(int, input().split())

    print(node,visited,V,E)
    
""" 
1
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
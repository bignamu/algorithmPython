def solution(n, computers):
    answer = 0
    node = 0
    
    nodeli = []
    for i in range(n):
        for j in range(n):
            if computers[i][j] != computers[j][i]:
                computers[i][j] = 1
    while computers:

        network = []


        
        for i in range(len(computers)):
            if sum(computers[i]) == 1:
                network.append(node)

                nodeli.append(node)
                node += 1
                computers.pop(0)
                network.pop()
                break
            for j in range(i+1,len(computers)):
                if computers[i][j] == 1:
                    if i not in network:
                        network.append(i)
                    if j not in network:
                        network.append(j)


        if network and len(computers) > 1:
            for _ in range(len(network)):
                computers.pop(0)
        elif len(network) == 0 and len(computers) >= 1:
            continue
        else:
            break
        nodeli.append(network)            
        node += 1    

        if len(computers) == 1 and n-1 not in network:
            nodeli.append(n-1)          
            node += 1
            break
    print('network', network,'\n',node,'\n','nodeList', nodeli)

    answer = node
    return answer

	
n = 5
computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]]

solution(n,computers)

# 실패 테스트데이터는 행렬 대칭이 아님


# saintgo9's solution
''' 
def solution(n, computers):
    answer = 0

    visited = [0] * n

    def next(computers, n):
        tmp = []
        for i in range(len(computers)):
            if computers[n][i] == 1:
                tmp.append(i)
        return tmp

    for i in range(n):
        if visited[i] == 0:
            answer += 1
            q = deque()
            visited[i] = 1
            for nex in (next(computers, i)):
                q.append(nex)
            while q:
                #print(q)
                ne = q.popleft()
                #print(ne) # 0 1
                if visited[ne] == 0:
                    visited[ne] = 1
                    for nex in next(computers, ne):
                        q.append(nex)

    return answer
'''

'''
bfs를 사용하여 순회를 한 번 하고 나면 
같은 네트워크상의 visited가 모두 갱신되기 때문에 
bfs를 도는 조건으로 방문하지 않았을 때를 설정하게 된다면
(visited가 1이므로 방문하지 않는다는 뜻) 서로 단절된 그래프는 
따로 방문하게 되고 따라서 bfs를 사용하는 조건(visited가 0이라는 뜻)이 
충족되어 순회에 들어가기 전에 count를 증가시켜 주면 
network의 개수를 구할 수 있다.

즉 네트워크마다 bfs가 순회를 따로 돌기 때문에 
bfs 순회에 들어가는 조건이 만족되면 다른 네트워크라는 뜻이므로 
count를 증가시키면 count의 값이 답이 된다.

'''


# 프로그래머스 답 BFS임 DFS아님
''' 
def solution(n, computers):
    answer = 0
    visited = [0 for i in range(n)]
    def bfs(computers, visited, start):
        stack = [start]
        while stack:
            j = stack.pop()
            if visited[j] == 0:
                visited[j] = 1
            for i in range(0, len(computers)):
                if computers[j][i] ==1 and visited[i] == 0:
                    stack.append(i)
    i=0
    while 0 in visited:
        if visited[i] ==0:
            bfs(computers, visited, i)
            answer +=1
        i+=1
    return answer 
    
'''
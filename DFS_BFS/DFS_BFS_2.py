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
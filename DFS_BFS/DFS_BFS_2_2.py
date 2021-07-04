import copy

def solution(n, computers):
    answer = 0
    idx = 0
    compu = 0
    noli = []    
    print(computers)
    for i in range(n):
        for j in range(n):
            if computers[i][j] != computers[j][i]:
                computers[i][j] = 1
    print(computers)   

    while computers:
        q = []
        previous = []
        head = computers.pop(0)
        idx = 0
        if sum(head) == 1:
            noli.append(q)
            continue
   
        for i in range(idx,n):
            if head[i] == 1 and i != idx:
                q.append(i)
        idx += 1
                    
        if q:
            noli.append(q)



    print(noli)
        
    print(len(noli))
    answer = len(noli)
            
    return answer

	
n = 5
computers = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 1], [0, 0, 1, 0, 1], [0, 0, 0, 1, 1], [1, 0, 0, 0, 1]] # 아웃풋 1

solution(n,computers)


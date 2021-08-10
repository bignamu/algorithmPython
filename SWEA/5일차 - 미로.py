from collections import deque

T = int(input())

for test_case in range(1, T + 1):
    
    N = int(input())
    matrix = []
    # 상하좌우
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for nn in range(N):
        line = list(map(int,input()))
        if 2 in line:
            # print(N-1)
            x = nn
            y = line.index(2)
        matrix.append(line)
    
    visited = [ [0]*N for _ in range(N)]
    what = 0
    def bfs(x,y):
        global what
        q = deque()
        q.append((x,y))
        visited[x][y] = 1    
        while q:
            x, y = q.popleft()
            
            for n in range(4):
                nx = x+dx[n]
                ny = y+dy[n]
                if nx >= N or nx<0 or ny>=N or ny <0:
                    continue
                if matrix[nx][ny] == 1:
                    continue
                if not matrix[nx][ny] and not visited[nx][ny]:
                    bfs(nx,ny)
                
                if matrix[nx][ny] == 3:
                    print(f'#{test_case}',1)
                    what = (nx,ny)
        return what
    answer = bfs(x,y)
    
    if not answer:
        print(f'#{test_case}',0)
            


''' 
1
5
13101
10101
10101
10101
10021
 '''
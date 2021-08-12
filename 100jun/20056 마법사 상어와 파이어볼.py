# https://www.acmicpc.net/problem/20056


N,M,K = map(int,input().split())


matrix = [[0]*(N+1) for _ in range(N+1)]


dx = [-1,1,0,0]
dy = [0,0,-1,1]
fireball = []
for _ in range(M):
        
    r,c,m,s,d = map(int,input().split())
    # matrix[r][c] = 1
    fireball.append((r,c,m,s,d))

while K:

    
    K -= 1
    matrix = [[0]*(N+1) for _ in range(N+1)]
    for idx, data in enumerate(fireball):

        r,c,m,s,d = data
        if not m:
            continue
        if d == 0:
            r = r + s *dx[0]
        elif d == 1:
            r = r + s *dx[0]
            c = c + s*dy[3]
        elif d == 2:
            c += s*dy[3]
        elif d == 3:
            r += s*dx[1]
            c += s*dy[3]
        elif d == 4:
            r += s*dx[1]
        elif d == 5:
            r += s*dx[1]
            c += s*dy[2]
        elif d == 6:
            c += s*dy[2]
        elif d == 7:
            r += s*dx[0]
            c += s*dy[2]
        fireball[idx] = (r,c,m,s,d)

        if r == 0:
            r = N
        elif r >N:
            if r//N:
                r = r//N
            else:
                r = N
        if c == 0:
            c = N
        elif c > N:
            if c//N:
                c = c//N
            else:
                c = N

        if matrix[r][c] and isinstance(matrix[r][c][0],int):
            
            matrix[r][c] = (matrix[r][c],(m,s,d))
        elif matrix[r][c]:
            empty = ()
            for em in matrix[r][c]:
                empty += em
            empty += (m,s,d)
        else:
            matrix[r][c] = (m,s,d)
        
    fireball = []

    for i in range(1,N+1):
        for j in range(1,N+1):
            if isinstance(matrix[i][j],int):
                continue
            elif isinstance(matrix[i][j][0],int):
                fireball.append((i,j,)+matrix[i][j])
            if len(matrix[i][j]) >= 2 and isinstance(matrix[i][j][0],tuple):
                
                total_m = 0
                total_s = 0
                length = len(matrix[i][j])
                test = []
                newd = []
                for ij in matrix[i][j]:
                    m,s,d = ij
                    total_m += m
                    total_s += s
                    test.append(d%2)
                if 0 in test and 1 in test:
                    newd = [1,3,5,7]
                else:
                    newd = [0,2,4,6]
                total_m = int(total_m / 5)
                total_s = int(total_s / length)

                if not total_m:
                    continue

                for nd in range(4):
                    fireball.append((i,j,total_m,total_s,newd[nd]))

answer = 0
for an in fireball:
    _,_,m,_,_ = an
    answer += m

print(answer)
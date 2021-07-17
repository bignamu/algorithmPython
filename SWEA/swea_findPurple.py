# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do





# https://swexpertacademy.com/main/solvingProblem/solvingProblem.do





T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    length = int(input())     
    matrix = [[0]*10 for _ in range(10)]


    for l in range(length):
        paint = list(map(int, input().split()))
        if paint[-1] == 1:
            dx = abs(paint[0] - paint[2])
            frontx = max([paint[0],paint[2]])
            backx = min([paint[0],paint[2]])
            dy = abs(paint[1] - paint[3])
            fronty = max([paint[1],paint[3]])
            backy = min([paint[1],paint[3]])
            for x in range(backx,frontx+1):
                for y in range(backy,fronty+1):
                    if matrix[x][y] == 2:
                    	matrix[x][y] = 3
                    elif matrix[x][y] != 3:
                        matrix[x][y] = 1
        if paint[-1] == 2:
            dx = abs(paint[0] - paint[2])
            frontx = max([paint[0],paint[2]])
            backx = min([paint[0],paint[2]])
            dy = abs(paint[1] - paint[3])
            fronty = max([paint[1],paint[3]])
            backy = min([paint[1],paint[3]])
            for x in range(backx,frontx+1):
                for y in range(backy,fronty+1):
                    if matrix[x][y] == 1:
                    	matrix[x][y] = 3
                    elif matrix[x][y] != 3:
                        matrix[x][y] = 2
                    
    purplelist = []
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                purplelist.append([i,j])

    print(f"#{test_case}",len(purplelist))
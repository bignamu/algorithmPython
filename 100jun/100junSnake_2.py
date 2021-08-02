# https://www.acmicpc.net/problem/3190

# 뱀 

# 게임이 끝나는 조건 벽에 부딪치거나 꼬리가 닿거나
import copy

N = 6
apple = 3

appleLocationList = [[3,4],[2,5],[5,3]] #[행,열] -1 해야함

leftRightInfoList = [[3,'D'],[15,'L'],[17,'D']]

boardMatrix = [[0]*(N+1) for _ in range(N+1)]

xpos = 1
ypos = 1
dx = [0,1,0,-1]
dy = [1,0,-1,0]

# 항상 동서남북을 하는것 아님
# 동남서북
time = 0
d = 0
tail = [[1,1]]

q = []
q.append((xpos,ypos,d))

while q:
    xpos,ypos,d = q.pop()
    x = xpos + dx[d]
    y = ypos + dy[d]

    t += 1

    if 1<=x<len(boardMatrix) and 1 <= y < len(boardMatrix):
        print(x,y)
        boardMatrix[x][y] += 1

        if boardMatrix[x][y] > 1:
            break
        if [x,y] not in appleLocationList:
            if tail:
                t = tail.pop(0)
        boardMatrix[t[0]][t[1]] -= 1
        tail.append([x,y])
        print(tail)
    else:
        tail.append([x,y])
        appleLocationList.remove([x,y])
    
    for di in leftRightInfoList:


# 2차원 배열에서 움직이는 가장 좋은 예제
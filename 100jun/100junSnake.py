""" # https://www.acmicpc.net/problem/3190

# 뱀 

# 게임이 끝나는 조건 벽에 부딪치거나 꼬리가 닿거나
import copy

N = 6
apple = 3

appleLocationList = [[3,4],[2,5],[5,3]] #[행,열] -1 해야함

leftRightInfoList = [[3,'D'],[15,'L'],[17,'D']]

boardMatrix = [[0]*N for _ in range(N)]
for rowcol in appleLocationList:
    boardMatrix[rowcol[0]-1][rowcol[1]-1] = 2

#print(boardMatrix)

directionArray= [[0,1],[0,-1],[1,0],[-1,0]] #동서남북 [dx][dy] 행의 변화,열의 변화

t = 0 # 초 측정
snake = [[0,0]]
previous = 0
for time, status in leftRightInfoList:
    if t == 0:
        while t<time:
            previous = snake
            snake[0][0] += directionArray[0][0]
            snake[0][1] += directionArray[0][1]
            if boardMatrix[snake[0][0]][snake[0][1]] == 2:
                previous

            t += 1
            break
    print(time,status)


print(boardMatrix,t)




 """

 # 못풀었음 핵심은 동서남북 dx dy로 표현가능하다


 # https://www.acmicpc.net/problem/3190

# 6
# 3
# 3 4
# 2 5
# 5 3
# 3
# 3 D
# 15 L
# 17 D

def simulation(room, apple_position, direct):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    time = 0
    d = 0
    xpos, ypos = (1, 1)
    q = []
    q.append((xpos, ypos, d))
    room[xpos][ypos] += 1
    tail = [[1, 1]]
    while q:
        xpos, ypos, d = q.pop(0)
        x = xpos + dx[d]
        y = ypos + dy[d]

        #show(room)

        time += 1
        if 1 <= x < len(room) and 1 <= y < len(room):
            # print(x, y)
            room[x][y] += 1

            if room[x][y] > 1:
                break

            if [x, y] not in apple_position:
                if tail:
                    t = tail.pop(0)
                room[t[0]][t[1]] -= 1
                tail.append([x, y])
                #print(tail)
            else:
                tail.append([x, y])
                apple_position.remove([x, y])

            for di in direct:
                if time == int(di[0]):
                    d = (d + 1)%4 if di[1] == 'D' else (d - 1)%4

            q.append((x, y, d))

    return time

def show(room):
    for i in range(1, len(room)):
        for j in range(1, len(room)):
            print(room[i][j], end=' ')
        print()
    print()

n = int(input())
k = int(input())

apple_position = [list(map(int, input().split())) for _ in range(k)]
#print(apple_position)

l = int(input())
direct = [list(input().split()) for _ in range(l)]
#print(direct)

room = [[0] * (n + 1) for _ in range(n + 1)]

print(simulation(room, apple_position, direct))
# https://www.acmicpc.net/problem/20055



N, K = map(int,input().split())

A_list = list(map(int,input().split()))

belt = [[0]*N for _ in range(2)]

robot = [0 for _ in range(N)]

for i in range(N):
    belt[0][i] = A_list.pop(0)
A_list.reverse()
belt[1] = A_list

# print(belt)
def rotate(_list):
    try:
        down = _list[0].pop()
        up = _list[1].pop(0)
        _list[0] = [up]+_list[0]
        _list[1] = _list[1] + [down]
        return _list
    except:
        temp = [0 for _ in range(N)]
        for i in range(0,N-1):
            temp[i+1] = _list[i]
        return temp


Ai = 0
cnt = 0
while Ai < K:
    Ai = 0
    if robot[N-1]:
        robot[N-1] = 0
    robot = rotate(robot)
    belt = rotate(belt)
    # cnt += 1
    if robot[N-1]:
        robot[N-1] = 0
    
    for i in range(N-1,-1,-1):
        if i - 1>=0 and belt[0][i] and not robot[i] and robot[i-1]:
            robot[i] = robot[i-1]
            robot[i-1] = 0
            belt[0][i] -= 1
    # cnt += 1
    
    if belt[0][0] and not robot[0]:
        robot[0] = 1
        belt[0][0] -= 1
    # cnt += 1

    cnt += 1
    for i in belt:
        for j in i:
            if not j:
                Ai += 1
                if Ai == K:
                    break


print(cnt)    
    
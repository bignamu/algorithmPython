# https://www.acmicpc.net/problem/14502
import sys
input = sys.stdin.readline

from copy import deepcopy

N,M = map(int,input().split())

labs = []
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]
virus = []

for n in range(N):

    labs.append(list(map(int,input().split())))
    for m,v in enumerate(labs[n]):
        if v==2:
            virus.append([n,m])
    


def possWall(arrvirus):
    arr=  []
    for v in arrvirus:
        x,y = v
        # print(x,y)
        for num in range(4):
            if x+dx[num] < 0 or x+dx[num] > N-1 or y+dy[num] < 0 or y+dy[num] > M-1:
                continue
            
            elif labs[x+dx[num]][y+dy[num]] != 0:
                continue
            arr.append([x+dx[num],y+dy[num]])
            
    print(arr)
    return arr

from collections import deque
def devour(labs):
    newlabs = deepcopy(labs)
    q = deque(virus)
    while q:
        x,y = q.popleft()
    
    
        
        # up
        if x+dx[0] >= 0:
            for up in range(x+dx[0],-1,-1):
                if newlabs[up][y] != 0:
                    break
                # print(up)
                newlabs[up][y] = 2
                
        # down
        if x+dx[1] < N:
            for down in range(x+dx[1],N):
                if newlabs[down][y] != 0:
                    break
                # print(down)
                newlabs[down][y] = 2
        
        # left
        if y+dy[2] >= 0:
            for left in range(y+dy[2],-1,-1):
                if newlabs[x][left] != 0:
                    break
                # print(left)
                newlabs[x][left] = 2
                
        # right
        if y+dy[3] < M:
            for right in range(y+dy[3],M):
                if newlabs[x][right] != 0:
                    break
                # print(down)
                newlabs[x][right] = 2
        
        for row in range(N):
            for col in range(M):
                if newlabs[row][col] == 0:
                    if row+dx[0] >=0 and newlabs[row+dx[0]][col+dy[0]] == 2:
                        q.append([row,col])
                        newlabs[row][col] = 2
                    elif row+dx[1] < N and newlabs[row+dx[1]][col+dy[1]] == 2:
                        q.append([row,col])
                        newlabs[row][col] = 2
                    elif col+dy[2] >=0 and newlabs[row+dx[2]][col+dy[2]] == 2:
                        q.append([row,col])
                        newlabs[row][col] = 2
                    elif col+dy[3] < M and newlabs[row+dx[3]][col+dy[3]] == 2:
                        q.append([row,col])
                        newlabs[row][col] = 2
                        
                        
                    
                    
    
    return newlabs
    

# print(devour())

    
    
    
    
    
# for lll in labs:
#     print(lll)

# for nll in devour(labs):
#     print(nll)

from itertools import combinations
from collections import Counter

allzero = []
for r in range(N):
    for c in range(M):
        if labs[r][c] == 0:
            allzero.append([r,c])


zeroCount = 0
for comb in combinations(allzero,3):
    newCount = 0
    newlabs = deepcopy(labs)
    # flag = False
    
    for x,y in comb:
        newlabs[x][y] = 1
    corrupted = devour(newlabs)
    
    for cor in corrupted:
        newCount += Counter(cor)[0]
        # if newCount > zeroCount:
            
        #     break
    
    if zeroCount < newCount:
        zeroCount = newCount
        

print(zeroCount)
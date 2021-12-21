# https://www.acmicpc.net/problem/21608

import sys
import math

input = sys.stdin.readline

N = int(input())
favor = dict()

for _ in range(N**2):
    _list = list(map(int,input().split()))
    favor[_list[0]] = _list[1:]

matrix = [ [0 for j in range(N)] for _ in range(N)]
favorMatrix = [ [0 for j in range(N)] for _ in range(N)]

# print(matrix)
# print(favor)
# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def maxVoidCount(x,y):
    count = 0
    
    for mv in range(4):
        if x+dx[mv]>=0 and x+dx[mv]<N and y+dy[mv]>=0 and y+dy[mv]<N and matrix[x+dx[mv]][y+dy[mv]] == 0:
            count += 1
            
    return count

def koi(fav):
    
    candi = []
    maxCount = -1
    for x in range(N):
        for y in range(N):
            
            if matrix[x][y] != 0:
                continue
            
            count = 0
            for mv in range(4):
                if x+dx[mv]>=0 and x+dx[mv]<N and y+dy[mv]>=0 and y+dy[mv]<N and matrix[x+dx[mv]][y+dy[mv]] in fav:
                    count += 1
            if count >= maxCount:
                maxCount = count
                candi.append([x,y,maxCount])
    candi = [ c for c in candi if c[2] == maxCount]

    if len(candi) == N**2:
        maxVoid = -1
        first_x = 0
        first_y = 0
        for ri,rv in enumerate(matrix):
            for ci,cv in enumerate(rv):
                if maxVoid < maxVoidCount(ri,ci):
                    maxVoid = maxVoidCount(ri,ci)
                    first_x = ri
                    first_y = ci
        
        return [[first_x,first_y,0]]
                    
    return candi
                        


for num,v in favor.items():
    
    result = sorted(koi(v),key=lambda x:(x[0],x[1]))
    flag = True
    if len(result) >1:
        
        test = list(map(lambda x:maxVoidCount(x[0],x[1]),result))
        if min(test) == max(test):
            final_x,final_y,_ = result[0]
            matrix[final_x][final_y] = num
            flag = False
        
        if flag:
            maxVoid = -1
            max_x = 0
            max_y = 0
            for r in result:
                rx,ry,_ = r
                counted = maxVoidCount(rx,ry)
                
                if maxVoid < counted:
                    maxVoid = counted
                    max_x,max_y = rx,ry
            final_x,final_y = max_x,max_y
            matrix[final_x][final_y] = num
    
    else:
        final_x,final_y,_ = result[0]
        matrix[final_x][final_y] = num
        
    
    
        

        
    
score = 0
for ri,rv in enumerate(matrix):
    for ci,cv in enumerate(rv):
        count = 0
        for mv in range(4):
            if ri+dx[mv]>=0 and ri+dx[mv]<N and ci+dy[mv]>=0 and ci+dy[mv]<N and matrix[ri+dx[mv]][ci+dy[mv]] in favor[cv]:
                count += 1
        if count == 2:
            score += 10
        elif count == 3:
            score += 100
        elif count == 4:
            score += 1000
        else:
            score += count
# print(matrix)
print(score)

        
        





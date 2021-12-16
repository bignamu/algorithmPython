# https://www.acmicpc.net/problem/18405

import sys

input = sys.stdin.readline

N, K = map(int,input().split())

contag = []
# numbers = []
_list = []

for i in range(N):
    inp = list(map(int,input().split()))
    contag.append(inp)
    for j in range(N):
        if contag[i][j]:
            _list.append([contag[i][j],0,i,j])

_list.sort()
    
S,X,Y = map(int,input().split())


# print(contag)

# 상하좌우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

from collections import deque

def bfs():

    q = deque(_list)
    

    while q:

        virus,sec,x,y = q.popleft()
        if sec == S:
            break
        for num in range(4):
            nx = x+dx[num]
            ny = y+dy[num]
            if nx>=0 and nx< N and ny >=0 and ny<N and contag[nx][ny] == 0:
                contag[nx][ny] = contag[x][y]
                q.append([virus,sec+1,nx,ny])
            
bfs()
    
# print(contag)
print(contag[X-1][Y-1])
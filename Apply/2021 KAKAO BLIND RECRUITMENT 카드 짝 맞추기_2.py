#https://www.youtube.com/watch?v=Q4bTSdi1psw
#https://programmers.co.kr/learn/courses/30/lessons/72415
import math



def solution(board, r, c):
    answer = math.inf
    mincnt = answer
    # 상하좌우
    moving = [(-1,0),(1,0),(0,-1),(0,1)]
    allcard = {}
    havetoremove = 1
    for i in range(4):
        for j in range(4):
            num = board[i][j]
            if num:
                havetoremove |= 1 << num
                if num in allcard:
                    allcard[num].append((i,j,0))
                else:
                    allcard[num] = [(i,j,0)]
    
    def permutate(cnt,removed,src):
        global answer

    print(allcard)
    print(havetoremove)
    
    
        
    
    
    return answer





board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
# 14

solution(board,r,c)
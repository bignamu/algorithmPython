

            

def solution(board, r, c):
    answer = 0
    enter = 1
    global cnt
    cnt = 0

    dx = [-1,1,0,0] # 상하좌우
    dy = [0,0,-1,1]
    def promising():
    
        return True

    def check(r,c):
        global cnt
        
        start = board[r][c]
        nxt_row = 0
        nxt_col = 0
        
        row_ctrl_down = 0
        for idx,num in enumerate(board):
            
            if start in num:
                nxt_row = idx
                nxt_col = num.index(start)

        print(r,c,nxt_row,nxt_col)

        
        if promising():
            print('hi')
        

    check(r,c)
        
    return answer





board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
# 14

solution(board,r,c)
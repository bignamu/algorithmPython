def solution(board):
    answer = 1234
    
    length = 0
    flag =False
    map = [rv for rv in board]
    # print(map)    
    for ri,rv in enumerate(board):
        for ci,cv in enumerate(rv):
            if ri==0 or ci == 0:
                if board[ri][ci]==1:
                    length = max(length,1)
                continue
            minimum = min(map[ri-1][ci],map[ri][ci-1],map[ri-1][ci-1])
            # minimum = min(minimum,map[ri-1][ci-1])

            if board[ri][ci]==1:
                map[ri][ci] = minimum+1
                length = max(length,map[ri][ci])
    answer = length**2
    print(answer)    
    return answer


board= [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]	 # answer = 9
solution(board)
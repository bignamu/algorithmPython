#https://programmers.co.kr/learn/courses/30/lessons/77485


def solution(rows, columns, queries):
    answer = []
    matrix = []
    count = 0
    _list = []
    for i in range(1,rows*columns+1):
        
        _list.append(i)
        count += 1
        
        if count%columns == 0 and i != 1:
            matrix.append(_list)
            _list = []
    # print(matrix,count)
    
    for q in queries:
        q = list(map(lambda x: x-1,q))
        x1,y1,x2,y2 = q
        
        # if x1==0 and y1==0 and x2==rows-1 and y2==columns-1:
        #     return [1]
        
        # print(q)
        up = []
        down = []
        left = []
        right = []
        for col in range(min(y1,y2),max(y1,y2)+1):
            up.append(matrix[min(x1,x2)][col])
            down.append(matrix[max(x1,x2)][col])
        for row in range(min(x1,x2),max(x1,x2)+1):
            left.append(matrix[row][min(y1,y2)])
            right.append(matrix[row][max(y1,y2)])
        # print(up,right,down,left)
        
        up= [left[1]] + up[:-1]
        right = [up[-1]] + right[:-1]
        down =  down[1:] + [right[-1]]
        left = left[1:]+ [down[0]]
        # print(up,right,down,left)
        
        answer.append(min(min(up),min(down),min(left),min(right)))
        
        for col in range(min(y1,y2),max(y1,y2)+1):
            matrix[min(x1,x2)][col] = up[col-min(y1,y2)]
            matrix[max(x1,x2)][col] = down[col-min(y1,y2)]
            
        for row in range(min(x1,x2),max(x1,x2)+1):
            matrix[row][min(y1,y2)] = left[row-min(x1,x2)]
            matrix[row][max(y1,y2)] = right[row-min(x1,x2)]
            
        
        
        
    # print(matrix)
    print(answer)
        
        

        
        
    return answer



rows= 100
columns=97
queries= 	[[1,1,100,97]]

solution(rows,columns,queries)
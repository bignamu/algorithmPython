import math

def solution(brown, yellow):
    answer = []
    totalSquare = brown + yellow
    def findheight(height):
        width = math.ceil(totalSquare / height)
        carpetMatrix = [[0]*(width+2) for _ in range(height+2)]
        #print(width,height)
        #print(carpetMatrix)
        for i in range(height+2):
            for j in range(width+2):
                if j == 0 or j == width+1:
                    carpetMatrix[i][j] = -1
                if i == 0 or i == height+1:
                    carpetMatrix[i][j] = -1
        
        yellowstk = yellow
        y_stk = 0
        for i in range (1,height+1):
            for j in range(1,width+1):
                for x in range(-1,2):
                    for y in range(-1,2):
                        if  carpetMatrix[i+x][j+y] == -1:         
                            y_stk += 1

                if y_stk > 0:
                    y_stk = 0
                elif yellowstk > 0:
                    carpetMatrix[i][j] = 1
                    yellowstk -= 1



        #print(carpetMatrix, yellowstk)

        cpstk = 0
        heightstk = 0
        for cp in carpetMatrix[1]:
            if cp == 0:
                cpstk += 1
        
        for h in range(1,height+1):
            heightstk += 1
        
        print(cpstk,heightstk,cpstk*heightstk,yellowstk,'wh', totalSquare)
        if totalSquare == cpstk*heightstk and yellowstk == 0:
            
            return [cpstk, heightstk]
        else:
            return -1

    for i in range(2,totalSquare):
        if totalSquare % i  != 0:
            continue
        if findheight(i) == -1:
            continue
        else:
            print(i)
            return findheight(i)

    
    return answer


brown = 5000
yellow = 25000

print(solution(brown,yellow))
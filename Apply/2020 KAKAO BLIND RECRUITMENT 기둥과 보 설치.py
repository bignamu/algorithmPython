# https://programmers.co.kr/learn/courses/30/lessons/60061

def solution(n, build_frame):
    answer = [[]]

    # 동서남북
    drow = [0,0,1,-1]
    dcol = [1,-1,0,0]

    

    matrix = [[0]*(n+1) for _ in range(n+1)]
    print(matrix)

    q = []
    

    for bf in build_frame:
        if bf[3] == 1 and bf[2] == 0: 
            if bf[1] == 0: # 바닥일 경우 기둥 바로 설치
                matrix[bf[1]][bf[0]] = 1
                continue
            if matrix[bf[1]-1][bf[0]] == 1: # 아래에 기둥이 있음
                matrix[bf[1]][bf[0]] = 1

            # 기둥 옆에 보가 1개만 있는지 검사
            if bf[0] != 0 and bf[0] != len(matrix)-1:
                if (matrix[bf[1]][bf[0]-1] == 2 and matrix[bf[1]][bf[0]+1] != 2) or (matrix[bf[1]][bf[0]+1] == 2 and matrix[bf[1]][bf[0]-1] != 2):
                    matrix[bf[1]][bf[0]] = 1

        # 보 건설
        if bf[3] == 1 and bf[2] == 1:
            # x가 0일때 보 설치 조건 오른쪽 아래에 기둥이 있나없나 없으면 +2
            if bf[0] == 0:
                if matrix[bf[1]-1][1] != 1:
                    matrix[bf[1]][bf[0]] = 2    
            # x가 끝값일때 보 설치 조건 오른쪽 아래에 기둥이 있나없나 없으면 +2
            if bf[0] == len(matrix)-1:
                if matrix[bf[1]-1][len(matrix)-2] != 1:
                    matrix[bf[1]][bf[0]] = 2                     
            
            # 양 옆에 보가 2개있는지 검사
            if bf[0] != 0 and bf[0] != len(matrix)-1:
                if (matrix[bf[1]][bf[0]-1] == 2 and matrix[bf[1]][bf[0]+1] == 2) or (matrix[bf[1]][bf[0]+1] == 2 and matrix[bf[1]][bf[0]-1] == 2):
                    matrix[bf[1]][bf[0]] = 2
            # 한쪽 끝 부분이 기둥 위에 있는지 검사
                if matrix[bf[1]-1][bf[0]] == 1: # 아래에 기둥이 있음
                    matrix[bf[1]][bf[0]] = 2

            # 한칸 아래 대각선으로 기둥이 있나 검사
                if (matrix[bf[1]-1][bf[0]+1] == 1 and matrix[bf[1]-1][bf[0]] != 1) or (matrix[bf[1]-1][bf[0]-1] == 1 and matrix[bf[1]-1][bf[0]] != 1):
                    matrix[bf[1]][bf[0]] = 2

        # 기둥 제거 
        if bf[3] == 0 and bf[2] == 0:
            if matrix[bf[1]+1][bf[0]-1] == 2 or matrix[bf[1]+1][bf[0]] == 2 or matrix[bf[1]+1][bf[0]+1] == 2:
                matrix[bf[1]][bf[0]] = 0
        # 보 제거
        if bf[3] == 0 and bf[2] == 1:
            if matrix[bf[1]-1][bf[0]-1] == 2 or matrix[bf[1]-1][bf[0]] == 2 or matrix[bf[1]-1][bf[0]+1] == 2:
                matrix[bf[1]][bf[0]] = 0

    print(matrix)
    for _ in range(len(matrix)):
        print(matrix.pop())


    return answer


n = 5	
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]

#[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]

solution(n,build_frame)



#기둥 바닥


""" 
기둥은 바닥 위에 있거나 보의 한쪽 끝 부분 위에 있거나, 또는 다른 기둥 위에 있어야 합니다.
보는 한쪽 끝 부분이 기둥 위에 있거나, 또는 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.

build_frame의 원소는 [x, y, a, b]형태

x, y는 기둥, 보를 설치 또는 삭제할 교차점의 좌표이며, [가로 좌표, 세로 좌표] 형태입니다.
a는 설치 또는 삭제할 구조물의 종류를 나타내며, 0은 기둥, 1은 보를 나타냅니다.
b는 구조물을 설치할 지, 혹은 삭제할 지를 나타내며 0은 삭제, 1은 설치를 나타냅니다.
 """
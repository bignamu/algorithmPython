def solution(n, build_frame):
    answer = [[]]

    matrix = [[0]*(n+1) for _ in range(n+1)]
    print(matrix)


    enableBo = []
    enableGi = []
    posi = []
    # for bf in build_frame:
    #     posi.append([bf[0],bf[1]])

    for bottom in range(len(matrix)):
        enableGi.append([bottom,0])


    # 
    while build_frame:
        scv = build_frame.pop(0)
        if scv[3] == 1 and scv[2] == 0: #기둥 설치
            for yesgi in enableGi:
                if yesgi == [scv[0],scv[1]]:
                        matrix[scv[1]][scv[0]] = 1
                        posi.append([scv[0],scv[1]])
                        enableGi.remove([scv[0],scv[1]])

                        enableGi.append([scv[0],scv[1]+1])
                        enableBo.append([scv[0],scv[1]+1])
                
        
        if scv[3] == 1 and scv[2] == 1: # 보 설치
            for yesbo in enableBo:
                if yesbo == [scv[0],scv[1]]:
                        matrix[scv[1]][scv[0]] = 2
                        posi.append([scv[0],scv[1]])
                        enableBo.remove([scv[0],scv[1]])

                        enableGi.append([scv[0]+1,scv[1]])

                

    print('Bo',enableBo,'Gi',enableGi,'Po',posi)
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
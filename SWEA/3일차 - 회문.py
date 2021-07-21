
import copy

T = int(input())


for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    matrix = []
    for i in range(N):
        nn = list(input().strip())
        matrix.append(nn)
    
    for i in range(N):
        for j in range(N-M+1):
            result = matrix[i][j:j+M]
            list_result = list(result)
            origin = copy.deepcopy(list_result)
            list_result.reverse()
            if list_result == origin:
                print(f'#{test_case}',''.join(result))
            
    for i in range(N):
        for j in range(N-M+1):
            result = []
            for mm in range(M):
                result += matrix[j+mm][i]
            list_result = list(result)
            origin = copy.deepcopy(list_result)
            list_result.reverse()
            if list_result == origin:
                print(f'#{test_case}',''.join(result))
    
"""   
1
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
 """
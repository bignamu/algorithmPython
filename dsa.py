from collections import deque
from itertools import combinations


def solution(n, info):
    
    answer=[]
    
    apeach = []
    
    for idx,l in enumerate(info):
        apeach.append((l+1,10-idx))
    
    # apeach[-1] = (0,0)
    # print(apeach)
    
    
    max_score = 0
    cur_list = []
    candidates = []
    prediff = 0
    result = 0
    for i in range(1,n+1):

        for permu in combinations(apeach,i):
            arrow = 0
            temp_score = 0
            temp_list = [0] * 10
            
            li_score = 0
            ap_score = 0
            for p in permu:
                arrow += p[0]
                temp_score += p[1]
            if arrow > n:
                continue
            
            for ppp in permu:
                temp_list[ppp[1] - 10] = ppp[0]
            
            i = 10
            for ap,li in zip(info,temp_list):
                
                if i <0:
                    break
            
                if ap >= li:
                    ap_score += i
                elif ap < li:
                    li_score +=  i
                i -= 1
                
            diff = li_score - ap_score
            
            if prediff < diff:
                prediff = diff
                result = diff
                cur_list.append(permu)
                    

    print(result,cur_list)
    
        
    
    
    
    return answer


n = 10
info = [0,0,0,0,0,0,0,0,3,4,3]

solution(n,info)

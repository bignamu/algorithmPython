from itertools import combinations
from collections import defaultdict
import bisect

def solution(info, query):
    answer = []
    _dict = defaultdict(list)

    for i in info:
        ii = i.split()
        score = int(ii[-1])
        ii = ii[:-1]
        for num in range(5):
            for cb in combinations(ii,num):
                joined = ''.join(cb)
                # print(joined)
                _dict[joined].append(score)
    # print(_dict)
    
    for d in _dict:
        _dict[d] = list(map(int,_dict[d]))
        _dict[d] = sorted(_dict[d])
        # print(_dict[d])
        
    for q in query:
        qlist = q.split(' ')
        qscore = int(qlist[-1])
        qlist = qlist[:-1]
        qlist = ''.join(qlist)
        while '-' in qlist or 'and' in qlist:
            if '-' in qlist:
                qlist = qlist.replace('-','')
            elif 'and' in qlist:
                qlist = qlist.replace('and','')
        
        

        

        fnd = _dict[qlist]
        start = 0
        end = len(fnd)
        
        while start < end:
            mid = (start+end)//2
            if fnd[mid] >= qscore:
                end = mid
            else:
                start = mid + 1
        # print(start,len(fnd))
                
        answer.append(len(fnd)-start)
            
        # print(qscore,fnd)

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info,query)
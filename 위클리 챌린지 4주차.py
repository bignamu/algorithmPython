# https://programmers.co.kr/learn/courses/30/lessons/84325?language=python3
# 2021 라인 상반기 기출

from collections import defaultdict

def solution(table, languages, preference):
    answer = ''
    _dict = defaultdict()
    
    for ta in table:
        tasplit = ta.split()
    
        for c in range(1,6):
            
            score = 6-c
            if tasplit[c] in languages:
                _dict[tasplit[0]+'_'+tasplit[c]] = score
    maxdict = defaultdict(list)
    for l,p in zip(languages,preference):
        for dname,dscore in _dict.items():
            if l == dname.split('_')[1]:
                dr = dname.split('_')[0]
                maxdict[dr].append(p * dscore)
    
    # for mx in maxdict.values():
        # print(sum(mx))

    maxdict = sorted(maxdict.items(),key=lambda x : sum(x[1]),reverse=True)
    
    check = []
    _, ds = maxdict[0]
    for nn,ss in maxdict:
        if sum(ds) == sum(ss):
            check.append(nn)
        else:
            break

    check.sort()
    # print(check)
    answer = check[0]
    
    # print(maxdict)
    # print(_dict)
    # print(answer)
    
    return answer



table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT", "C", "C++" ,"C#" , "SQL", "PYTHON", "KOTLIN", "PHP"]

preference = [10,10,10,10,10,10,10,10,10]

solution(table,languages,preference)
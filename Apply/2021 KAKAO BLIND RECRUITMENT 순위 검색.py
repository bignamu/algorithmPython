def solution(info, query):
    answer = []
    db = []
    qu = []
    # check = [1] * len(info)
    for _info in info:
        db.append(_info.split(' '))
    
    for _query in query:
        score = 0
        for i in range(1,len(_query)):
            if _query[-i] != '-'and not _query[-i].isalpha() and _query[-i].isnumeric():
                continue
            # print(i)
            score = _query[-i:].lstrip()
            _query = _query[:-i]
            break
        # print(score)
        _query = _query.split(' and ')
        _query.append(score)
        qu.append(_query)

    for q in qu:
        check = [1] * len(info)
        for num in range(5):
            for idx in range(len(info)):
                if num == 4 and check[idx] == 1:
                    if int(db[idx][4]) < int(q[4]):
                        check[idx] = 0
                    continue
                if q[num] not in '-' and q[num] != db[idx][num] and check[idx] == 1:
                    check[idx] = 0
                    continue
            
        # print(check)
        answer.append(sum(check))
    # print(answer)
    

    return answer


info = ["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

solution(info,query)

def solution(record):
    answer = []
    rec = []
    ids = []
    id_nick = []
    for i,r in enumerate(record):
        rsplit = r.split()
        rec.append([i]+rsplit)
        if not rsplit[1] in ids:
            ids.append(rsplit[1])
    rec = sorted(rec,key=lambda x:(x[2],x[0]),reverse=True)
    # print(rec)
    # print(ids)
    
    for i in ids:
        chk_list = list(filter(lambda x:x[2]==i,rec))
        # chk_list = sorted(chk_list,key=lambda x:x[0],reverse=True)
        # print(chk_list)
        for val in chk_list:
            if len(val) == 3:
                continue
            event = val[1]
            id = val[2]
            nick = val[3]
            if event == 'Enter' or event == 'Change':
                id_nick.append([id,nick])
                break
    
    # print(id_nick)
    
    for r in record:
        rsplit = r.split()
        event = ''
        if rsplit[0]=='Enter':
            event = '들어왔습니다.'
        elif rsplit[0] == 'Leave':
            event = '나갔습니다.'
        elif rsplit[0] == 'Change':
            continue

        for i,n in id_nick:
            if rsplit[1] == i:
                nick = n
                break

        result = f'{nick}님이 {event}'
        # print(result)
        answer.append(result)
            
        
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
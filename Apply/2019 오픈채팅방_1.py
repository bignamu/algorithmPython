
def solution(record):
    answer = []
    
    ids = {}
    
    for r in record:
        rsplit = r.split()
        print(rsplit)
        
        if len(rsplit) != 2:
            ids[rsplit[1]] = rsplit[2]
        
    print(ids)
    
    for r in record:
        rsplit = r.split()

        if rsplit[0]=='Enter':
            event = '들어왔습니다.'
        elif rsplit[0] == 'Leave':
            event = '나갔습니다.'
        elif rsplit[0] == 'Change':
            continue
        
        nick = ids[rsplit[1]]
        
        result = f'{nick}님이 {event}'
        
        answer.append(result)
        
    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
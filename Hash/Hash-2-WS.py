def solution(data):
    break_tf = False
    for i in data:
        a = data.remove(i)
        dd = [x for x in a if x.startswith(i)]
        if dd:
            break_tf = True
            answer = False
            break
    if not break_tf:
        answer = True

    return answer


li = ["12","123","1235","567","88"]

solution(li)
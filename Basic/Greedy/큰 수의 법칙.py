N,M,K = 5, 8, 3

_list = [2,4,5,4,6]
_list.sort()
_list.reverse()
_list = _list[0:2]
cntlist = [K,K]
answer = 0
while M:
    if _list[0] > _list[1]:
        answer += _list[0]
        cntlist[0] -= 1
        M -= 1
        if not cntlist[0]:
            answer += _list[1]
            cntlist[0] = K
            M -= 1
    elif _list[0] == _list[1]:
        answer = _list[0]*M
        break

print(answer)
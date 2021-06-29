def sol(numstr):
    answer = 0

    zeroCtn = 0
    ichiCtn = 0
    for i in numstr:
        if i == '0':
            zeroCtn += 1
        else:
            ichiCtn += 1

    print(zeroCtn,ichiCtn)

    front = numstr[0]
    state = []
    temp = 1
    for i in numstr[1:len(numstr)]:
        
        if i == front:
            temp += 1
            front = i
            continue
        elif i  != front:
            state.append([front,temp])
            temp = 1
            front = i
            continue

    state.append([front,temp])

    print(state)
    
    zeroGroup = 0
    ichiGroup = 0
    for i in state:
        if i[0] == '0':
            zeroGroup += 1
        else:
            ichiGroup += 1
    print(zeroGroup,ichiGroup)

    answer = min(zeroGroup,ichiGroup)
    return answer

numstr = '0000000000000000' # 1


print(sol(numstr))



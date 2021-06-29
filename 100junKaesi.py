def sol(numstr):
    answer = 0
    numLi = list(numstr)
    print(numLi)
    
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
    if front == '1':
        front == '0'
    elif front == '0':
        front == '1'
    state.append([front,temp])
    print(state)
    
    zeroGroup = 0
    ichiGroup = 0
    for i in state:
        if i[0] == '0':
            zeroGroup += 1
        else:
            ichiGroup += 1

    print (zeroGroup,ichiGroup)

    answer = min(zeroGroup,ichiGroup)
    print(answer)    
    return answer


numstr = '0000000000100000000' # 1


sol(numstr)


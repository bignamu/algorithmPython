def solution(N, number):
    answer = 0
    if N == number:
        return 1
    
    setList = [set() for _ in range(8) ]
    
    for idx, se in enumerate(setList,start=1):
        ini = int(str(N)*idx)
        se.add(ini)
    
    for i in range(1,8):
        for j in range(i):
            for op1 in setList[j]:
                for op2 in setList[i-j-1]:
                    setList[i].add(op1 + op2)
                    setList[i].add(op1 - op2)
                    setList[i].add(op1 * op2)
                    if op2 != 0:
                        setList[i].add(op1//op2)
        if number in setList[i]:
            answer = i + 1
            break
    else:
        answer = -1
    


    return answer



N = 5
number = 12

print(solution(N,number))

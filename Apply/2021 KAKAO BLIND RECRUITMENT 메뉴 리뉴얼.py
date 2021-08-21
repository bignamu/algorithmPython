
def solution(orders, course):
    answer = []
    
    for i in range(len(orders)):
        for j in range(i+1,len(orders)):
            result = set(orders[i]) & set(orders[j])
            result = list(result)
            if len(result) == 1 or not result:
                continue
            # result.sort()
            result = ''.join(result)
            answer.append(result)
    # for ans in answer:
        
    
    cbset = list(set(answer))
    cbset.sort()
    arr = [0] * len(cbset)
    for o in orders:
        flag = False
        for idx,cb in enumerate(cbset):
            flag = False
            for ccbb in cb:
                if ccbb not in o:
                    flag = True
                    break
            if not flag:
                arr[idx] += 1

    answer = []
    ccc = [0]*11
    for c in course:
        
        for m,n in zip(cbset,arr):
        
            if c == len(m):
                ccc[c] = max(ccc[c],n)

    for m,n in zip(cbset,arr):
        for c in course:
            if n == ccc[c] and len(m) == c:
                answer.append(m)
    print(cbset,arr,ccc)
    print(answer)

    return answer



orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
solution(orders,course)
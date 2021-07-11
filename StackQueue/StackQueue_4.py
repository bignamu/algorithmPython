def solution(prices):
    answer = []
    stk = [0] * len(prices)
    q = [[prices[0],0]] # 가격, 인덱스

    print(q)
    while q:
        temp_q = q.pop()
        for idx, prices in enumerate(prices):
            pricesq,idxq = temp_q
            if prices >= pricesq:
                stk[idxq] = 1
                stk[idx] = 1
                stk = stk.__add__(stk)
                q.append()
                q.append(prices.pop())

            else:
                stk[idxq] = 0
                stk[idx] = 1
                stk = stk.__add__(stk)
                
        

    return answer





prices = [1, 2, 3, 2, 3]

print(solution(prices))
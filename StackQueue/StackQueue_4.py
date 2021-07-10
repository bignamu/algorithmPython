def solution(prices):
    answer = []
    stk = [1] * len(prices)
    q = [[prices[0],0]] # 가격, 인덱스

    print(q,stk)
    while q:
        temp_q = q.pop()
        for idx, prices in enumerate(prices):
            pricesq,idxq = temp_q
            if prices >= pricesq:


        

    return answer





prices = [1, 2, 3, 2, 3]

print(solution(prices))
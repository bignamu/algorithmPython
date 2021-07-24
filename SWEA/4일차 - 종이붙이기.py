

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    N = N // 10
    _list = [0 for _ in range(N)]
    _list[0] = 1
    _list[1] = 3
    

    for i in range(2,N):
        _list[i] = _list[i-1] + 2*_list[i-2]
    
    print(f'#{test_case}',_list[-1])
    # def paper(val):
        
    #     pa = [1,3]

    #     if val == 1:
    #         return pa[0]
    #     elif val == 2:
    #         return pa[1]
    #     else:
    #         for i in range(3,val+1):
    #             pa.append(paper(i-1) + 2 * paper(i-2))
    #         return pa[-1]

    # print(f'#{test_case}',paper(N))
    
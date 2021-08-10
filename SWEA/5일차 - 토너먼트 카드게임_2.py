from collections import deque

# 분할 정복 문제
#숫자 1은 가위, 2는 바위, 3은 보를 나타낸다

T = int(input())

for test_case in range(1, T + 1):

    N = int(input())
    
    def test(_list):
        test = []
        for i,num in enumerate(_list):
            test.append((num,i))
        return test

    _list = list(map(int, input().split()))
    _list = test(_list)
    # print(_list)
    # exit()
    # visited = [0] * N
    def rsp(i,you):
        if i == 1:
            if you == 2:
                return you
            else:
                return i
        elif i == 2:
            if you == 3:
                return you
            else:
                return i
        elif i == 3:
            if you == 1:
                return you
            else:
                return i

    def dv(li):
        q = deque()
        q.append(li)
        while q:
            qq = q.popleft()
            if len(qq) > 2:
                half = len(qq) // 2
                
                nn1,ii1 = dv(qq[:half])
                nn2,ii2 = dv(qq[half:])
                if nn1 != rsp(nn1,nn2):
                    return (nn2,ii2)
                    
                else:
                    return (nn1,ii1)
                    
                
            elif len(qq) == 2:
                n1,i1 = qq[0]
                n2,i2=  qq[1]
                if n1 != rsp(n1,n2):
                    return (n2,i2)
                else:
                    return (n1,i1)
            elif len(qq) == 1:
                a,b = qq[0]
                return (a,b)

            
        
    print(f'#{test_case}',dv(_list)[1]+1)



''' 
3
4
1 3 2 1
6
2 1 1 2 3 3
7
1 3 3 3 1 1 3
 '''
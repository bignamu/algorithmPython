T = int(input())

for test_case in range(1, T + 1):
    p,a,b = map(int, input().split())    
    l = 1
    r = p
    pp = p

    def findPage(l,r,a):
        cnt = 0
        while 1:
            c = int((l+r)/2)
            cnt += 1
            if c < a:
                l = c            
            elif c > a:
                r = c
            elif c == a:
                break
        return cnt
    cnta = findPage(l,r,a)

    l = 1
    r = pp
    cntb = findPage(l,r,b)

    if cnta> cntb:
        print(f"#{test_case}","B")
    elif cnta < cntb:
        print(f"#{test_case}","A")
    else:
        print(f"#{test_case}","0")
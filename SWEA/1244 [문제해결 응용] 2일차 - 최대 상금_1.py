
import copy

T = int(input())

for test_case in range(1, T + 1):
    mny, cnt=input().split()
    
    q = [mny]

    for _ in range(int(cnt)):
        cur = []
        while q:
            qpop = q.pop()
            for start in range(len(qpop)-1):
                end = start+1
                while end < len(qpop):
                    lm = list(qpop)
                    lm[start], lm[end] = lm[end],lm[start]
                    lmjoined = ''.join(lm)
                    cur.append(lmjoined)
                    end += 1
        q = copy.deepcopy(set(cur))
        print(q)
    cur = map(int,cur)
    print(f'#{test_case}',max(cur))

        


''' 
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
'''


for tc in range(1,int(input())+1):
    data, K = input().split() # 숫자판의 정보, 교환횟수
    K = int(K)
    N = len(data)
    now = set([data])
    nxt = set()
    for _ in range(K):
        while now:
            s = now.pop()
            s = list(s)
            for i in range(N):
                for j in range(i+1,N):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s))
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now

    print('#{} {}'.format(tc,max(map(int,now))))


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
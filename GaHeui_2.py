import sys

N, M = map(int,sys.stdin.readline().rstrip().split())


keywordlist = []
boradlist = []
keywordused = [0] * N
# print(keywordused)
for _ in range(N):
    keywordlist.append(sys.stdin.readline().rstrip())

for _ in range(M):
    boradlist.append(sys.stdin.readline().rstrip())

for b in boradlist:
    blist = b.split(',')
    for bb in blist:
        if bb in keywordlist:
            idx = keywordlist.index(bb)
            if keywordused[idx] != 1:
                keywordused[idx] = 1
    cnt  = 0
    for used,key in zip(keywordused,keywordlist):
        if used == 0:
            cnt += 1
    print(cnt)
            
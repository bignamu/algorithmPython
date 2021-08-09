# https://www.acmicpc.net/problem/14916

n = int(input())

cnt = 0

coin = [5,2]
max5 = n // 5
max2 = n // 2
cntlist = []
for i in range(max5+1):
    for j in range(max2+1):
        if 5*i + j*2 == n:
            cntlist.append(i+j)
if cntlist:
    print(min(cntlist))
else:
    print(-1)
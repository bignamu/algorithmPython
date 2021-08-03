# https://www.acmicpc.net/problem/14501

import copy


N = int(input())



tli = [0]
pli = [0]
dp = [0] * (N+1)
ndp = [0] * (N+1)
for i in range(0,N):
    T, P = map(int,input().split())
    tli.append(T)
    pli.append(P)

for i in range(N,0,-1):
    able = N-i+1
    if i+tli[i] > N:
        if i+1 > N:
            dp[i] = 0
        else:
            dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1],pli[i]+dp[i+tli[i]])

print(dp)



""" 
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
 """
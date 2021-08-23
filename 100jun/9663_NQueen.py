# https://www.acmicpc.net/problem/9663


N = int(input())



col = [0]*N # queen[row] = col

global cnt
cnt = 0
def promising(i,col):
    k = 0
    flag = True
    while(k<i and flag):
        if (col[i]==col[k] or abs(col[i]-col[k])==i-k):
            flag = False
        k += 1
    return flag
def dfs(i,col):
    global cnt
    if promising(i,col):
        if (i==N-1):
            # print(col[:])
            cnt += 1
        else:
            for j in range(N):
                col[i+1] = j
                dfs(i+1,col)


dfs(-1,col)
print(cnt)
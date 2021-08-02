# https://www.acmicpc.net/problem/13458

N = int(input())

Ai = list(map(int,input().split()))

B, C = map(int,input().split())


# print(N,Ai,B,C)
def mns(num):
    return num - B

test = list(map(mns,Ai))

count = 0
cant = 0
for t in test:
    if t>=1:
        if t % C:
            count += t // C
            count += 1
        else:
            count += t // C

count += len(test)
print(test,count)

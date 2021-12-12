# https://www.acmicpc.net/problem/19539

appleTree = [0]*int(input())

want = list(map(int,input().split()))

# print(sum(want)%3,sum(want))
val = 0

for i in want:
    val += i // 2 
print(val,sum(want),sum(want)//3)
if(not sum(want)%3 and val>=sum(want)//3):
    print('YES')
else:
    print('NO')



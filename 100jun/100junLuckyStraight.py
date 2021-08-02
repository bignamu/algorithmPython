# https://www.acmicpc.net/problem/18406

# 


luckyli = []

for i in input():
    luckyli.append(int(i))

length = len(luckyli)

left = 0
right = 0

for i in luckyli[0:int(length/2)]:
    left += i

for j in luckyli[int(length/2):]:
    right += j

print(left,right)
if left == right:
    print("LUCKY")
else:
    print("READY")



import sys
import copy

N,M = map(int,sys.stdin.readline().rstrip().split())

blist = []
for _ in range(N):
    blist.append(list(map(int,sys.stdin.readline().rstrip().split())))

atklist = []
for _ in range(M):
    atklist.append(list(map(int,sys.stdin.readline().rstrip().split())))


# print(blist,atklist)

pre_x = 0
pre_y = 0

while atklist:
    atk = atklist.pop(0)
    atkx,atky,atkhp = atk
        
        
        
    a = (atky-pre_y)/(atkx-pre_x)
    b = atky - a* atkx
    bcopy = []
    for idx, bval in enumerate(blist):
        bx,by,bhp = bval
        if by == (a*bx + b):
            bhp -= atkhp
            if bhp >0:
                bcopy.append([bx,by,bhp])
    
    # pre_x = atkx
    # pre_y = atky
    blist = copy.deepcopy(bcopy)

hp = 0
for bhp in blist:
    hp += bhp[2]
# print(blist,atklist,hp)
print(hp)
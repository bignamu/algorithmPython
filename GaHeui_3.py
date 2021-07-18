import sys
import copy

N,T,W = map(int,sys.stdin.readline().rstrip().split())

t = 0

nlist = []

nT = 0
for n in range(N):
    npx,npt = map(int,sys.stdin.readline().rstrip().split())
    if npt >= T and n != 0:
        nT += 5
    elif npt < T and n != 0:
        nT += npt
    nlist.append([npx,npt,nT])

M = int(sys.stdin.readline().rstrip())

q = []
mlist = []
for _ in range(M):
    mlist.append(list(map(int,sys.stdin.readline().rstrip().split())))
    
mlist.sort(key=lambda x : x[2])
# for m in range(M):
#     mlist[m].pop()

print(nlist,mlist)

for npx,npt,npc in nlist:
    for i in range(1,T+1):
        t += 1
        npt -= 1
        print(npx)
        if npt == 0:
            break
    if npt:
        npc += 5
        q.append([npx,npt,npc])


for px,pt,pc in mlist:
    for qx,qt,qc in q:
        if qc < pc:
            for i in range(1,T+1):
                t += 1
                pt -= 1
                print(px)
                if pt == 0:
                    break
        else:
            for i in range(1,T+1):
                t += 1
                qt -= 1
                print(qx)
                if qt == 0:
                    break
            
    if pt:
        pc += 5
        q.append([px,pt,pc])

print(q)
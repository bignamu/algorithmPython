# https://www.acmicpc.net/problem/21608

from typing import Sequence


N = int(input())

suki = [0 for _ in range(N**2+1)]
seq = [0 for _ in range(N**2+1)]

x33 = [[0]*3 for _ in range(3)]

for i in range(N**2):
    _list = list(map(int,input().split()))
    suki[_list[0]] = _list[1:]
    seq[i+1] = _list[0]
    
print(suki)

cls = [[0]*(N+2) for _ in range(N+2)]

print(cls,seq)

def search3x3(row,col):
    r = [row-1,row,row+1]
    c = [col-1,col,col+1]
    nochair = 0
    for i in r:
        for j in c:
            if i and j and i != N+1 and j != N+1:
                if not cls[i][j]:
                    nochair += 1
    return nochair
            
        

while seq:
    skip = False
    jk = seq.pop(0)
    if not jk:
        cls[2][2] = seq.pop(0)
        continue
    for i in range(1,N+1):
        for j in range(1,N+1):
            for luv in suki[1:]:
                if skip:
                    break
                for ll in luv:
                    if cls[i][j] == ll:
                        temp = [0 for _ in range(4)]
                        r1 = i+1
                        c1 = j
                        if not cls[r1][c1]:
                            temp[0] = search3x3(r1,c1)
                        r2 = i-1
                        c2 = j
                        if not cls[r2][c2]:
                            temp[1] = search3x3(r2,c2)
                        r3 = i
                        c3 = j+1
                        if not cls[r3][c3]:
                            temp[2] = search3x3(r3,c3)
                        r4 = i
                        c4 = j-1
                        if not cls[r4][c4]:
                            temp[3] = search3x3(r4,c4)
                        maxx = max(temp)
                        
                        ibox = []
                        rbox = [r1,r2,r3,r4]
                        cbox = [c1,c2,c3,c4]
                        for idx,tem in enumerate(temp):
                            if tem == maxx:
                                
                                ibox.append(idx)
                                
                        curr = rbox[ibox[0]]
                        curc = cbox[ibox[0]]
                        if len(ibox) >= 2:
                            
                            for ii in range(1,len(ibox)):
                                if curr > rbox[ibox[ii]]:
                                    curr = rbox[ibox[ii]]
                                    curc = cbox[ibox[ii]]
                            cls[curr][curc] = jk
                            skip = True
                            break
                                
                        cls[rbox[idx]][cbox[idx]] = jk
                        skip=True
                    
                

print(cls,seq)
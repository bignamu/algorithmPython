# https://www.acmicpc.net/problem/15686


import copy #copy.deepcopy()
from itertools import combinations
def sol(chickenMatrix,M):
    lenchic = len(chickenMatrix)
    chictrix = copy.deepcopy(chickenMatrix)

    chicli = []
    for i in range(lenchic):
        for j in range(lenchic):
            if chictrix[i][j] == 2:
               chicli.append([i,j]) 
    
    #print(chicli)

    decoy = []
    for i in range(lenchic):
        for j in range(lenchic):
            if chictrix[i][j] == 1:
                decoy.append([i,j])
    #print(decoy ,'decoy')
                
    
    combli = list(combinations(chicli,M))
    chickenStreetList = []
    sumStreetList = []
    #print(combli)
    for comb in range(len(combli)):
        for deco in range(len(decoy)):
            try:
                eachChikenStreet = min(
                abs(combli[comb][0][0] - decoy[deco][0]) + abs(combli[comb][0][1] - decoy[deco][1]),
                abs(combli[comb][1][0] - decoy[deco][0]) + abs(combli[comb][1][1] - decoy[deco][1])
                )
                chickenStreetList.append(eachChikenStreet)
            except:
                eachChikenStreet = abs(combli[comb][0][0] - decoy[deco][0]) + abs(combli[comb][0][1] - decoy[deco][1])
                
                chickenStreetList.append(eachChikenStreet)
        sumStreetList.append(sum(chickenStreetList))
        chickenStreetList = []
    #print(sumStreetList,min(sumStreetList))
    answer = min(sumStreetList)
    return answer

inp = '''5 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1
1 2 0 2 1'''

chickenMatrix = []

inpt = inp.split('\n')

N = int(inpt[0][0])
M = int(inpt[0][2])

inpt = inpt[1:]
#print(inpt)

for i in inpt:
    tori = []
    for j in i:
        if j != ' ' and j != '\n':
            tori.append(int(j))
            #print(j)
    chickenMatrix.append(tori)

#print(chickenMatrix)
# chikenMatrix.append(inp.split('\n'))

print(sol(chickenMatrix,M ))
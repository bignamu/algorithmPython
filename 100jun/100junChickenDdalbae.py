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


N, M = map(int,input().split())


chickenMatrix = []

for _ in range(N):
    chickenMatrix.append(list(map(int,input().split())))



print(sol(chickenMatrix,M))
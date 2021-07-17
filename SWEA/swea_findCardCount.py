



T = int(input())
# T = 1
for test_case in range(1, T + 1):
    length = input()
    # length = 10
    cardSet = list(map(int, input()))
    # cardSet = list(map(int,str(08271)))
    
    cntList = [0]*10
    for i in range(0,10):
        if cardSet.count(i):
            cntList[i] = cardSet.count(i)
    idx = max(cntList)
    maxList = []
    for i in range(0,10):
        if cntList[i] == idx:
            maxList.append(i)
    
    print(f"#{test_case}",max(maxList),idx)
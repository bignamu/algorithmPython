def solution(answers):
    
    answer = []
    p1 = answers[:]   
    p2 = answers[:]
    p3 = answers[:]
    
    for i in range(1,len(answers)+1):
        if i % 5 == 0:
            p1[i-1] = 5
            continue
        p1[i-1] = (i % 5)

    for i in range(len(answers)):
        if i == 0:
            p2[i] = 2
            continue
        
        if i % 8 == 1:
            p2[i] = 1
        elif i % 8 == 3:
            p2[i] = 3
        elif i % 8 == 5:
            p2[i] = 4
        elif i % 8 == 7:
            p2[i] = 5


        if i % 2 == 0:
            p2[i] = 2
    
    temp = 0
    for i in range(len(answers)):
        if i == 0:
            p3[i] = 3
            temp += 1
            continue
        
        if temp == 1 or temp == 0:
            p3[i] = 3
            temp += 1
        elif temp == 2 or temp == 3:
            p3[i] = 1
            temp += 1
        elif temp == 5 or temp == 4:
            p3[i] = 2
            temp += 1
        elif temp == 7 or temp == 6:
            p3[i] = 4
            temp += 1
        elif temp == 9 or temp == 8:
            p3[i] = 5
            temp += 1

        if temp == 10:
            temp = 0

    
    xa , ya, za = 0, 0, 0
    for x,y,z,a in zip(p1,p2,p3,answers):
        if x == a:
            xa += 1
        if y == a:
            ya += 1
        if z == a:
            za += 1
    ansDict = {1:xa,
                2:ya,
                3:za}
    lidi = dict(sorted(ansDict.items(),key = lambda x : -x[1]))
    
    rtn = []
    
    for idx in lidi:
        firstIdx = lidi.get(idx)
        firstKey = idx
        lidi.pop(idx)
        break

    
    rtn.append(firstKey)
    for idx in lidi:
        if firstIdx > lidi.get(idx):
            break
        elif firstIdx == lidi.get(idx):
            rtn.append(idx)
        
        firstIdx = lidi.get(idx)


        
    print(xa,ya,za)
    print(rtn)

    answer = rtn
    return answer


answers = [1, 3, 2, 4, 2]

solution(answers)


# 길어진 이유 enumerate() 몰라서
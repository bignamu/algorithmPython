def solution(n, lost, reserve):
    answer = 0
        
    count = {}
    for i in range(1,n+1):
        count[i] = 1

    for lo in lost:
        count[lo] -= 1

    for re in reserve:
        count[re] += 1

    print('계산전 : ', count)

    for i in range(1,n+1):
        if (i != 1 and i != n):
            if count[i] == 0:
                if count[i+1] ==2:
                    count[i+1] -= 1
                    count[i] += 1
                if count[i-1] ==2:
                    count[i-1] -= 1
                    count[i] += 1

        if i == 1:
            if count[i+1] == 2:
                count[i+1] -= 1
                count[i] += 1
        if i == n:
            if count[i-1] == 2:
                count[i-1] -= 1
                count[i] += 1
        

    print(count, list(count.values()))

    temp = 0
    for val in count.values():
        if val == 0:
            temp += 1

    print(temp)

    answer = n - temp


    return answer



n = 3
lost = [3]
reserve = [1]

solution(n,lost,reserve)


# 프로그래머스 답
""" def solution(n, lost, reserve):
    _reserve = [r for r in reserve if r not in lost]
    _lost = [l for l in lost if l not in reserve]
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost) """

# saitngo9's solution
''' 
_dict = {}
_list = []

a = [4, 5, 6, 5, 4, 3]

for i in a:
    _dict[i] = 0

for i in a:
    _dict[i] += 1

_sorted = dict(sorted(_dict.items()))

_sorted2 = (sorted(_sorted.items(), key=lambda x: x[1]))

print(_sorted)
print(_sorted2)

for i in _sorted2:
    for j in range(i[1]):
        print(i[0], end=' ') '''
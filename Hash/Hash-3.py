from itertools import combinations

def solution(clothes):
    answer = 1
    dict = {}

    for tu in clothes:
        dict[tu[0]] = tu[1]
    dict = sorted(dict.items(),key=lambda x:x[1])

    print(dict)


    return answer


li = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]

solution(li)
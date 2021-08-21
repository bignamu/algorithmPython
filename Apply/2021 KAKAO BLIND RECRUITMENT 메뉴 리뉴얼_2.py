from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    
    for c in course:
        candidates = []
        for o in orders:
            for cb in combinations(o,c):
                joined = ''.join(sorted(cb))
                candidates.append(joined)
        counter_candi = Counter(candidates).most_common()
        answer += [menu for menu,cnt in counter_candi if cnt > 1 and cnt == counter_candi[0][1]]
        answer.sort()

    return answer

orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
course = [2,3,5]
print(solution(orders,course))
from itertools import combinations

def solution(numbers, target):
    answer = 0
    diff =  target - sum(numbers)
    comstk = 0
    
    for i in range(1,len(numbers)):
        comb = list(combinations(numbers,i))
        for j in range(len(comb)):
            if sum(list(comb[j]))*(-2) == diff:
                comstk += 1

    

    
    answer = comstk
    return answer



numbers = [1, 2, 1, 1, 1] # 5
target = 3	

solution(numbers,target)

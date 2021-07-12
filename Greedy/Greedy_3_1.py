#7월 12일 stack
# https://programmers.co.kr/learn/courses/30/lessons/42883?language=python3
def solution(number, k):
    answer = 0
    
    list_num = list(map(int,list(number)))
    k = abs(len(number) - k)
    stack = [list_num.pop(0)]
    
    while list_num:
        
        num_pop = list_num.pop(0)
        s_pop = stack.pop()
        
        if num_pop > s_pop and len(stack) < k:
            stack.append(num_pop)
            stack.append(list_num)
        elif num_pop < s_pop and len(stack) < k:
            stack.append(s_pop)
            stack.append(list_num.pop(0))
        elif num_pop == s_pop and len(stack) <k:
            stack.append(num_pop)
            stack.append(s_pop)
            stack.append(list_num.pop(0))
            
            
    answer = stack

    return answer 

number = "4177252841"	
k = 4	#"775841"

print(solution(number,k))
""" def solution(number, k):
    answer = ''
    return answer


number = "4177252841"	
k = 4	#"775841"
arr = list(number)

start = 0
temp = 0
 
print(sorted(number))


 """

# 프로그래머스 solution
def solution(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)

number = "4177252841"	
k = 4	#"775841"

solution(number,k)
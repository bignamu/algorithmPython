def solution(letters, k):
    stack = [letters[0]]

    k = len(letters) - k
    for num in letters[1:]:
        while len(stack) > 0 and ord(stack[-1]) < ord(num) and k > 0:
            k -= 1
            
            
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:k]


    return ''.join(stack)



letters = "aaaaaaaaaazxy"	
k = 3	

"zgj"

print(solution(letters,k))
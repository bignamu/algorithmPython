import re




T = int(input())

for test_case in range(1, T + 1):

    strr = input()
    
    lsr = list(strr)
    stack = [lsr[0]]
    flag = False
    
    for s in range(1,len(lsr)):
        if stack[-1] != lsr[s]:
            stack.append(lsr[s])
        elif stack[-1] == lsr[s] and len(stack) >= 2:
            stack.pop()
        elif stack[0] == lsr[1] != lsr[2]:
            flag = True
    if flag:
        stack.pop(0)
    # print(stack)

    print(f'#{test_case}',len(stack))

                
            
    
    
""" 
3
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX
 """
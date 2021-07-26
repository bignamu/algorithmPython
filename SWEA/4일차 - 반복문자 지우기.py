import re




T = int(input())

for test_case in range(1, T + 1):

    strr = input()
    strr = list(strr)
    stack = [strr[0]]
    flag = 0
    while strr:
        qq = strr.pop(0)
        stack.pop()
        for s in strr:
            if qq != s:
                stack.append(qq)
                stack.append(s)
                break
            elif qq == s:
                break
    print(stack)    
    
""" 
1
ABCCB
NNNASBBSNV
UKJWHGGHNFTCRRCTWLALX
 """
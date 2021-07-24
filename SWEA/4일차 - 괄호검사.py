

T = int(input())

for test_case in range(1, T + 1):
    raw=input()
    stack = []
    mode = False

    for r in list(raw):

        if (not stack and r == '}') or (not stack and r == ')'):
            print(f'#{test_case}',0)
            mode = True
            break
        if stack:
            if (stack[-1] == '(' and r == '}') or (stack[-1] == '{' and r == ')'):
                mode = True
                break

        if r == '(' or  r =='{':
            stack.append(r)
        elif r == ')' and stack[-1] == '(':
            stack.pop()
        elif r == '}' and stack[-1] == '{':
            stack.pop()

    if stack:
        print(f'#{test_case}',0)
    elif not stack and not mode:
        print(f'#{test_case}',1)
            

""" 
3
print('{} {}'.format(1, 2))
N, M = map(int, input().split())
print('#{} {}'.format(tc, find())
 """
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    _list = list(input().split())
    stack = []
    symbol = ['/','+','*','-']
    flag = False
    flag2 = False
    for l in _list:

        if l == '.':
            if len(stack)>=2:
                print(f'#{test_case}','error')
                flag2 = True
                break    
            # stack.append(l)
            flag = True
            break
        elif l not in symbol:
            stack.append(l)

        elif l in symbol and not flag:

            try: 
                t = float(stack.pop())
                f = float(stack.pop())
                if l == symbol[0]:
                    result = f/t
                elif l == symbol[1]:
                    result = f + t
                elif l == symbol[2]:
                    result = f * t
                elif l == symbol[3]:
                    result = f - t

                stack.append(result)
            except:
                print(f'#{test_case}','error')
                flag2 = True
                break

    if stack and stack[0] != '.':
        test = int(str(stack[0]).split('.')[-1])
        if stack[-1] == '.' and not test:
            print(f'#{test_case}',int(stack[0]))
        else:
            print(f'#{test_case}',stack[0])
    elif not flag2:
        print(f'#{test_case}','error')


    



''' 
3
10 2 + 3 4 + * .
5 3 * + .
1 5 8 10 3 4 + + 3 + * 2 + + + .
 '''
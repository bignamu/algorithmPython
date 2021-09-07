from collections import Counter

def solution(p):
    answer = ''
    
    def promise(p):
        test = []
        for pp in p:
            if not test:
                test.append(pp)
                continue
            if pp == '(':
                test.append(pp)
            if '(' in test and pp == ')':
                test.pop()
        if test:
            return False
        elif not test:
            return True
    



    def dfs(start):

        if not start:
            return ''
        stk = []
        end = 0
        for s in start:
            if not stk:
                stk.append(s)
                end += 1
                continue
            stk.append(s)
            stk2 = Counter(stk)
            end += 1
            if stk2['('] == stk2[')']:  
            
                    
                break
        
        u = ''.join(stk)
        v = start[end:]


        if promise(u):
            return u + dfs(v)
        else:
            
            u = u[1:]
            u = u[:-1]
            new_u = ''
            for uu in u:
                if uu == '(':
                    new_u += ')'
                elif uu == ')':
                    new_u += '('
            new_v = dfs(v)
            return '('+new_v+')'+new_u



        
    # print(dfs(p))
    answer = dfs(p)
    return answer




p = "()))((()"		# result "()(())()"
solution(p)
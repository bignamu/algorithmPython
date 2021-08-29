# https://programmers.co.kr/learn/courses/30/lessons/60057
import math

def solution(s):
    answer = math.inf
    
    
    mx = len(s)//2
    for i in range(1,mx+1):
        start = 0
        end = i
        all = []
        while start<len(s):
            all.append(s[start:end])
            start += i
            end += i

        ans = ''
        while all:

            popped = all.pop(0)
            cnt = 1
            for i in range(len(all)):
                if popped == all[i]:
                    cnt += 1
                else:
                    break
            if cnt > 1:
                for _ in range(cnt-1):
                    all.pop(0)
                ans += f'{cnt}{popped}'
            elif cnt == 1:
                ans += popped
        if answer > len(ans):
            answer = len(ans)
        
    print(answer)

    answer = min(len(s),answer)
        
    print(answer)

        


    
    

    return answer


s = "ababcdcdababcdcd"	# 14
solution(s)
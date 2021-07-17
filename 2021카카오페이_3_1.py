

import re
# print('SUBMARINE' if re.compile('(100+1+|01)+').fullmatch(input()) else 'NOISE')




def solution(line1, line2):
    answer = 0
    length1 = len(line1)
    length2 = len(line2)
    addLength = length2 -1
    ableCount = 0
    while 1:
        
        if length2 <= length1:
            ableCount += 1
            length2 += addLength
        if length2 > length1:
            break

    length2 = len(line2)
    
    for ablecnt in range(0,ableCount):
        
        dot = '.'*ablecnt
        dottedline2 = dot.join(line2)
        print(dottedline2)
        dottedlength2 = len(dottedline2)
        for i in range(length1-dottedlength2+1):           
            compare = line1[i:dottedlength2+i]
            
            if re.compile(dottedline2).match(compare):
                answer += 1



    return answer


line1 = "abcabcabc"
line2 = "abc"


print(solution(line1,line2))
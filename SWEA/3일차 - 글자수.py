import re


T = int(input())

for test_case in range(1, T + 1):
    str1 = input().rstrip()
    str2 = input().rstrip()
    cnt = []
    for i in list(set(str1)):
        if re.findall(i,str2):
            result = re.findall(i,str2)
            cnt.append(len(result))
    answer = max(cnt)
    print(f'#{test_case}',answer)




""" 
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
"""
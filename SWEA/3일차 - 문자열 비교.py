
T = int(input())

for test_case in range(1, T + 1):
    
    str1 = input().rstrip()
    str2 = input().rstrip()
    length1 = len(str1)
    length2 = len(str2)
    check = 0
    for i in range(length2-length1+1):
        if str2[i:i+length1] == str1:
            print(f'#{test_case}',1)
            check += 1
            break
    
    if not check:
        print(f'#{test_case}',0)

""" 
3
XYPV
EOGGXYPVSY
STJJ
HOFSTJPVPP
ZYJZXZTIBSDG
TTXGZYJZXZTIBSDGWQLW
 """
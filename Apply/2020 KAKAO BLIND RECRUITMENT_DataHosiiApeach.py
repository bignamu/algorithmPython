''' 

def solution(s):
    answer = 0
    sli = list(s)

    length = len(s)
    halflen = int(length/2)
    
    
    def intoJail(cnt,length):
        jail = []
        for i in range(0,halflen):
            jail.append(''.join(sli[i*cnt:i*cnt+cnt]))
            print(jail)       
        
        # for i in jail:
        #     if len(i) != cnt:
        #         jail.pop(i)  
        #     print(jail)

        # for i in jail:
        #     if len(i) == cnt:
        #         jail = jail[jail.index(i):]
        #         break
        # for i in range(-1,-length,-1):
        #     if len(jail[i]) == cnt:
        #         jail = jail[0:(len(jail) + i+1)]
        #         break
        
        return jail

    stk = 0
    temp = '-1'
    templi = []
    rtnli = []
    for i in range(3,4):
        rtnJail = intoJail(i,length)
        print(intoJail(i,length))


        for j in range(0,len(rtnJail)):


            try:
                if rtnJail[j] == rtnJail[j+1]:
                    
                    #print(j)
                    temp = rtnJail[j]
                    stk += 1
                    #print(temp, stk)
                    continue
            except:
                print(' ')
                #print(stk, temp, templi, rtnJail)

            if stk == 0:
                templi.append(rtnJail[j])

            if stk != 0:
                templi.append('{}{}'.format(stk+1,temp))
                stk = 0
                temp = '-1'
                print(temp, stk)
        
        rtnli.append(''.join(templi))
        templi = []
    
        print(rtnli)
    # rtnli.sort(key=lambda x :len(x))
    # print(len(rtnli[0]))    

    # answer = len(rtnli[0])

    return answer


s = "aabbaccc" # 14

print(solution(s)) '''


# 실패

def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    print(words)
    print(words[1:] + [''])
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    print(res)
    print(sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res))
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    print(list(range(1, int(len(text)/2) + 1)) + [len(text)])
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])

a = [
    "aabbaccc",
    "ababcdcdababcdcd",
    "abcabcdede",
    "abcabcabcabcdededededede",
    "xababcdcdababcdcd",

    'aaaaaa',
]

for x in a:
    print(solution(x))
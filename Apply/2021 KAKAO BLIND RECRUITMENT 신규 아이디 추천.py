import re

def solution(new_id):

    answer = ''
    new_id = new_id.lower()
    
    for word in new_id:
        if word.isalnum() or word in '-_.':
            answer += word
    
    while '..' in answer:
        answer = answer.replace('..','.')

    answer = answer[1:] if answer[0] == '.' and len(answer) >1  else answer
    answer = answer[:-1] if answer[-1] == '.' else answer
    
    if not answer:
        answer = 'a'
    
    if len(answer) >= 16:
        answer = answer[:15] 

        answer = answer[:-1] if answer[-1] == '.' else answer
    
    if len(answer) <= 2:
        lastword = answer[-1]
        while len(answer)<3:
            answer += lastword

    print(answer)
    return answer



new_id = "z-+.^."
solution(new_id)
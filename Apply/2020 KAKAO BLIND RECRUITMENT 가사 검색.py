import re

def solution(words, queries):
    answer = []
    
    for query in queries:
        p = re.compile('[?]')
        sub_query = p.sub('.',query)
        cnt = 0
        for w in words:
            if len(w) == len(query):
                test_w = re.compile(sub_query).match(w)
                if test_w:
                    cnt += 1
                
        answer.append(cnt)
        
    return answer




words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]	
queries = ["fro??", "????o", "fr???", "fro???", "pro?","?????"]
#	[3, 2, 4, 1, 0]

print(solution(words,queries))
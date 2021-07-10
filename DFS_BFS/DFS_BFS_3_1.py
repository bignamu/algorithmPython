#프로그래머스 답임 못풀었음 BFS아직 잘 몰라
# https://programmers.co.kr/learn/courses/30/lessons/43163

# sum([True,True,False]) => True의 개수를 반환해줌 

def solution(begin, target, words):
    answer = 0
    Q = [begin]
    
    while True:
        temp_Q = []
        for word_1 in Q:
            if word_1 == target:
                return answer
            for i in range(len(words)-1,-1,-1):
                word_2 = words[i]
                if sum([x!=y for x,y in zip(word_1,word_2)]) == 1:
                    temp_Q.append(words.pop(i))
        if not temp_Q:
            return 0
        Q = temp_Q
        answer += 1
    return answer


begin = "hit"
target = "cog"
words = ["hot", "dot", "dog", "lot", "log", "cog"]

print(solution(begin,target,words))
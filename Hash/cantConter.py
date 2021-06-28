import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]


participant = ["leo", "kiki", "eden", "leo"]
completion = ["eden", "kiki", "leo"]




print(solution(participant, completion))
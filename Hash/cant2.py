# https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3




def solution(participant, completion):
    dict = {}
    for partPeople in participant:
        if dict.get(partPeople):
            dict[partPeople] += 1
        else:
            dict[partPeople] = 1

    for comPeople in completion:
        if dict.get(comPeople):
            dict[comPeople] -= 1

    for partPeople in participant:
        if dict.get(partPeople) == 1:
            return partPeople
        




participant = ["leo", "kiki", "eden", "leo"]
completion = ["eden", "kiki", "leo"]

print(solution(participant, completion))


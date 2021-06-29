def solution(people, limit):
    answer = 0
    return answer


people = [70, 50, 80, 50]
limit = 100



boat = 0



while(1):
    if len(people) == 0:
        break

    stack = [people[0]]
    for p in people[1:]:
        if sum(stack)+p <= limit:
            stack.append(p)

    for st in stack:
        people.remove(st)
    boat += 1
    
print(stack)
print(people, boat)
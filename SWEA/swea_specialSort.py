T = int(input())

for test_case in range(1, T + 1):
    length = int(input())
    number = list(map(int, input().split()))

    answer = []
    number.sort()
    while number:
        maxx = number.pop()
        minn = number.pop(0)
        answer.append(maxx)
        answer.append(minn)
    if len(answer) > 10:
        answer = answer[:10]
    answer = list(map(str,answer))
    answer = " ".join(answer)
    
    print(f"#{test_case}",answer)
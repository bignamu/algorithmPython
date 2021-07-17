



T = int(input())
# T = 1
for test_case in range(1, T + 1):
    length,M = map(int, input().split())
    # length = 10
    # M = 3
    serial = list(map(int, input().split()))
    # serial = [1,2,3,4,5,6,3,8,9,10]
    cal = []
    
    for i in range(length-M):
        temp = 0
        for j in range(M):
            temp += serial[i+j]
        cal.append(temp)

    answer = max(cal)-min(cal)

    print(f"#{test_case}",answer)
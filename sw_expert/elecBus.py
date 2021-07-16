# 3
# 3 10 5
# 1 3 5 7 9
# 3 10 5
# 1 3 7 8 9
# 5 20 5
# 4 7 9 14 17

# 한번 충전으로 최대한 이동할 수 있는 정류장 수 K
# 충전기가 설치된 M개의 정류장 번호
# 버스는 0번에서 출발해 종점인 N번 정류장까지 이동

# K N M
# M개의 충전소가 설치된 정류장 번호

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    K,N,M = map(int, input().split())
    charge_list = [0]*10
    charge = list(map(int, input().split()))
    previous = 0


    for c in charge:
        charge_list[c] = 1
    cnt = 0
    while 1:
        for i in range(previous+K,previous,-1):
            if charge_list[i] == 1:
                previous = i + K
                cnt += 1
                break
        if previous>10:
            print(f"#{test_case}",cnt)
            break


    print(charge_list)
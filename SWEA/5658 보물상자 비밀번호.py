# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo

# import sys


T = int(input())

for test_case in range(1, T + 1):

    N, K = map(int, input().split())

    arr = list(input())

    n = N/4
    maps = []

    for nn in range(int(n)):
        maps.append(arr[-nn:]+arr[:-nn])

    candi = set()
    for i in range(N):
        val = '0x'
        for j in range(int(n)-1, -1, -1):
            val += maps[j][i]

        val2 = int(val, 16)
        candi.add(val2)
    candi = list(candi)
    candi.sort(reverse=True)
    print(f'#{test_case} {candi[K-1]}')

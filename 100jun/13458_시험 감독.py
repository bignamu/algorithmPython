# https://www.acmicpc.net/problem/13458

# import sys
# input = sys.stdin.readline


n = int(input())


a = list(map(int, input().split()))

b, c = map(int, input().split())


cnt = 0


def sol():
    global cnt
    new_a = list(map(lambda x: x-b, a))

    for v in new_a:

        cnt += 1
        if v > 0:
            cnt += v//c
            if v % c:
                cnt += 1


sol()
print(cnt)

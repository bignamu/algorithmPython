# https://www.acmicpc.net/problem/14889

N = int(input())

matrix = []

for _ in range(N):
    stat = list(map(int,input().split()))
    matrix.append(stat)

print(matrix)

def two():
    
N = input().split(' ')
M = int(N[1])
N = int(N[0])

_list = list(map(int, input().split()))


answer = 0

interval_sum = 0
end = 0

for start in range(N):
    while interval_sum < M and end < N:
        interval_sum += _list[end]
        end += 1
    if interval_sum == M:
        answer += 1
    interval_sum -= _list(start)


    
print(answer)
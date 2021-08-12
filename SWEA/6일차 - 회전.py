from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    N ,M = map(int,input().split())
    q = deque()

    _list = list(map(int,input().split()))

    a = _list.pop(0)
    _list.append(a)

    print(f'#{test_case}',_list)
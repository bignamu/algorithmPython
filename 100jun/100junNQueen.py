# https://www.acmicpc.net/problem/9663

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    L = int(input())      
    N = int(input())      
    origin = []
    loss = [0] # 0은 0으로 이동한다 1은 0에서 1로 이동한다
    for n in range(N):
        s, e = map(int, input().split())
        origin.append([s,e])
        if n != 0:
            loss.append(s - pre_e)
        pre_e = e

    print(origin,len(origin),loss)


    # while origin:


""" 
1
5
2
2 5
6 10
 """
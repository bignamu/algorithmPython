# https://www.acmicpc.net/problem/14501

import copy


N = int(input())



_list = [0] * (N+1)
for i in range(0,N):
    T, P = map(int,input().split())
    if T+i <= N and not _list[T+i]:
        _list[T+i] = P
    elif T+i <= N and _list[T+i]:
        if isinstance(_list[T+i],int):
            _list[T+i] = [_list[T+i],P]
            continue
        temp = []
        for ti in  _list[T+i]:
            temp.append(ti)
        _list[T+i] = temp

print(_list)
    
    






""" 
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200
 """
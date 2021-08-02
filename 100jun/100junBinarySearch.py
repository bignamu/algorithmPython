
""" 

N = input()
Nlist = list(map(int,input().split()))

M = input()
Mlist = list(map(int, input().split()))

print(N,M,Nlist,Mlist) """



M = 5
N = 5
Nlist = [4, 1, 5, 2, 3]
Mlist = [1, 3, 7, 9, 5]


from sys import stdin
import bisect

n = int(stdin.readline())
a = list(map(int, stdin.readline().split()))

m = int(stdin.readline())
x = list(map(int, stdin.readline().split()))

a.sort()

for j in x:
    if a[bisect.bisect(a, j) - 1] == j:
        print(1)
    else:
        print(0)

        
""" def bs(a, target):
    low = 0
    high = len(a) - 1
    mid = 0
    while low <= high:
        mid = (low + high) // 2
        if a[mid] > target:
            high = mid - 1
        elif a[mid] < target:
            low = mid + 1
        else:
            break
    return mid """

#https://www.acmicpc.net/problem/1920

""" 
이진 탐색이란?
이진 탐색이란 데이터가 정렬돼 있는 배열에서 특정한 값을 찾아내는 알고리즘이다. 
배열의 중간에 있는 임의의 값을 선택하여 찾고자 하는 값 X와 비교한다. 
X가 중간 값보다 작으면 중간 값을 기준으로 좌측의 데이터들을 대상으로, 
X가 중간값보다 크면 배열의 우측을 대상으로 다시 탐색한다. 
동일한 방법으로 다시 중간의 값을 임의로 선택하고 비교한다. 
해당 값을 찾을 때까지 이 과정을 반복한다.

 """
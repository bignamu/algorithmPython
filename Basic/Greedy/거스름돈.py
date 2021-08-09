""" 
500
100
50
10
"""

coin = [500,100,50,10]

N = int(input())
cnt = 0
while coin:
    co = coin.pop(0)
    
    if N//co:
        cur = N // co
        cnt += cur
        N = N - co*cur

print(cnt)
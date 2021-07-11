# https://www.acmicpc.net/problem/10872

import timeit
start_time = timeit.default_timer() 

already = [0,1]

def facto(x):

    if x == 1:
        return 1
        
    return x*facto(x-1)


def facto_dp(n):
    
    if n == 0:
        return 1
    elif n == 1:
        return 1
    facto_array = [0,1]
    num = 1
    for i in range(2,n+1):
        num *= i
    facto_array.append(num)
    return num

print(facto_dp(10000))
terminate_time = timeit.default_timer()
print("%f초 걸렸습니다." % (terminate_time - start_time))

""" n = int(input())

def fac(n):
    if n == 1:
        return 1
    else:
        return n * fac(n - 1)

print(fac(n)) """
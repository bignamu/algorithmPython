# https://www.acmicpc.net/problem/11005


_input = input().split(' ')

def numsys(n,b):
    _list = []
    while n >= b:
        if b > 10 and n % b >= 10:
            _list.append(chr((n%b)+55))
        else:
            _list.append(str(n % b))
        n = n//b
    
    if b > 10 and n >= 10:
        _list.append(chr(n+55))
    else:
        _list.append(str(n))
    return _list
    
answer = numsys(int(_input[0]),int(_input[1]))
answer.reverse()

print(''.join(answer))
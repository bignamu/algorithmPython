
_input = '10010111'

import re
print('SUBMARINE' if re.compile('(100+1+|01)+').fullmatch(input()) else 'NOISE')
        


#https://www.acmicpc.net/problem/2671
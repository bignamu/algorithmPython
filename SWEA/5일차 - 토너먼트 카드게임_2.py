def sol(st, en):
    selection = [st, en]
    solve = [[0], [0, 0, 1, 0], [0, 0, 0, 1], [0, 1, 0, 0]]
    res = solve[data[st]][data[en]]
    return selection[res]
 
def div(start, end):
    if start == end:
        return start
    st = div(start, (start+end)//2)
    en = div((start+end)//2 + 1, end)
    return sol(st, en)
 
 
TC = int(input())
for tc in range(1, TC+1):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    result = div(1, N)
    print("#%d %d"%(tc, result))

# 7월 7일
# 두 리스트간의 중복을 제거할 때는 list(set()-set())을 쓰자
# 어디에 있다는 무조건 in 또는 not in
def solution(n, lost, reserve):
    answer = 0
    _reserve = list(set(reserve) - set(lost))
    _lost = list(set(lost) - set(reserve))
    for r in _reserve:
        f = r - 1
        b = r + 1
        if f in _lost:
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
        
    return n - len(_lost)

n = 5
lost = [2, 4,5]	
reserve = [1, 3, 5]

solution(n,lost,reserve)


''' 주어진 정수형 배열에 저장되어 있는 원소들의 빈도수를 계산하고, 
각 원소 별 빈도수 오름차순 + 원소 오름차순으로 정렬하여 출력하라. 
예로써 int[] a = { 4, 5, 6, 5, 4, 3 } 이라는 배열이 input으로 입력되면, 
{ 3, 6, 4, 4, 5, 5 } 로 정렬 된 결과가 출력된다. 
정렬 및 출력 순서는 값의 크기보다 빈도수를 우선으로 한다. '''


_dict = {}
_list = []

a = [ 4, 5, 6, 5, 4, 3 ]


for i in a:
    _dict[i] = 0

for i in a:
    _dict[i] += 1

_sorted = dict(sorted(_dict.items()))

_sorted2 = dict(sorted(_sorted.items(),key = lambda x:x[1]))


print(_sorted)
print(_sorted2)

for i in _sorted2:
    while (_sorted2[i]>0):
        _sorted2[i] -= 1
        _list.append(i)
    
print(_list)
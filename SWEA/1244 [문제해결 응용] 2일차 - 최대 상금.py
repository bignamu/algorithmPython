from itertools import permutations

T = int(input())

for test_case in range(1, T + 1):

    plate, cnt = map(int, input().split())
    plate = list(map(int,str(plate)))

    while cnt:

        nome = set(permutations(plate,len(plate))).difference(plate)
        
        # print(nome)
        # print(max(nome))
        plate = list(max(nome))

        cnt -= 1
    plate = ''.join(map(str,plate))
    print(f'#{test_case}',plate)


''' 
10
123 1
2737 1
757148 1
78466 2
32888 2
777770 5
436659 2
431159 7
112233 3
456789 10
'''
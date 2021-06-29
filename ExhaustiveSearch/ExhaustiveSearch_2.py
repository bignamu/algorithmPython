def solution(numbers):

    from itertools import permutations
    import math
    answer = 0

    def isPrime(number):
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return 0
        return 1
    prli = []

    print(isPrime(49))

    for i in range(1,len(numbers)+1):
        prli += list(permutations(numbers,i))

    print(prli)
    combstr = ''
    combli = []
    for i in set(prli):
        for j in list(i):
            combstr += j
        combli.append(int(combstr))
        combstr=''
    
    lisetcombli = list(set(combli))
    print(lisetcombli)

    
    
    
    rtn = 0
    for co in lisetcombli:
        print(co)
        if co == 1:
            continue
        elif co == 0:
            continue
        temp = isPrime(co)
        rtn += temp
        
    print(rtn)

    answer = rtn

    return answer



numbers = "011" #return 2
solution(numbers)

# 알아야할 것
# from itertools import permutations
#    int(math.sqrt(number)) + 1

#에라토스테네스 체
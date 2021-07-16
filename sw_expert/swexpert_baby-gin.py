# 파이썬 SW문제해결 기본 - LIST1
# https://swexpertacademy.com/main/learn/course/lectureVideoPlayer.do#none

from itertools import permutations
from itertools import combination_with_itertools

def solution(number):

    # number.sort()
    # triple = 0
    # if len(set(number[:3])) == 1:
    #     triple += 1
    # if len(set(number[3:])) == 1: 
    #     triple += 1
    
    # run = 0
    # cnt = 0
    # for i in range(len(number)-1):
    #     ii = i+1
    #     if i<3 and abs(number[i] - number[ii]) == 1:
    #         cnt += 1
    #     elif i>=3 and abs(number[i] - number[ii]) == 1:
    #         cnt += 1
    #     else:
    #         cnt = 0
        
    #     if cnt == 2:
    #         run += 1

    # if triple+run == 2:
    #     return "Baby-gin"

    # return "fail"
    # print(list(set(permutations(number,6))))
    print(list(set(combination_with_itertools(number,6))))
    return 0

number = input()
number = list(map(int,number))
print(solution(number))
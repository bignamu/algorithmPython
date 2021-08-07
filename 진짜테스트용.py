
import os
import argparse


print(os.path.dirname('H:\Resources\Algorithm\Python\kakaopay04-4.png').split('\\')[-1])

print(min(1,0))

p = 'is'
t = 'This is a book~!'

M = len(p)
N = len(t)

def BruteForce(p,t):
    i = 0
    j = 0
    while j < M and i < N:
        if t[i] != p[j]:
            i= i - j
            j = -1

        i += 1
        j += 1
    if j == M:
        return i-M
    else:return -1


print(BruteForce(p,t))

a = type('abc')
print(a.__name__)




A_list = ['a', 'b', 'c'] 
B_list = ['d', 'e', 'c', 'd', 'e', 'f']

clist = A_list+B_list
print('C_List',clist)

A_set = set(A_list)
B_set = set(B_list)
C_set = A_set | B_set
print('C_set',C_set)
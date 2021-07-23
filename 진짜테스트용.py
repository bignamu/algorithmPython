import sys
import re


str1 = 'ABCA'
str2 = 'ABABCA'

for i in list(str1):
    print(re.findall(i,str2))




_list = [1,'abc','b']

print(_list['abc'])
import os
from glob import glob
import re
path = os.path.dirname(os.path.realpath(__file__))
print(path)

# _list = glob(os.path.join(path,'*'))
_list = os.listdir(path)
print(_list)

ignoreList = []
for l in _list:
    print(l)

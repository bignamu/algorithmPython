import sys
import copy

start_time = sys.stdin.readline()
N = int(sys.stdin.readline())

sec = start_time.split(':')
h = int(sec[0])*3600
m = int(sec[1])*60
s = int(sec[2])

sec = h + m + s


train = []
for _ in range(N):
    f, b, time = sys.stdin.readline().split()
    time = time.split(':')
    h = int(time[0])*3600
    m = int(time[1])*60
    train.append([f,b,h+m])



special =[ 
['K210',3],
['K221',4],
['K225',3],
['K245',4],
['K249',4],
['K256',3],
['K221',4],
['K223',3],
['K239',3],
['K248',5],
['K251',3],
['K267',3]
]

train_time = {}
chk = []
for i in range(210,273):
    name = f'K{i}'
    train_time[name] = 120


for name,time in special:
    train_time[name] = time*60


for idx,(start,end,time) in enumerate(train):
    start_tnum = int(start[-3:])
    end_tnum = int(end[-3:])
    if end_tnum > 272:
        end = 'K272'
    pre_check = time
    ttime = 0
    for tt in range(start_tnum,end_tnum-1):
        ttime += train_time[f'K{tt}'] + 20
        check_time = time + ttime    
        if pre_check <= sec <= check_time:
            print(start,end,tt,idx)
            tolast = ttime
        pre_check = check_time
    if tolast:
        ttime -= tolast
        chk.append(ttime)
        tolast = 0
answer = sec+min(chk)
ansh = answer // 3600

answer = answer - ansh * 3600
ansm = answer // 60

ansmm = answer - ansm * 60

print(f'{ansh}:{ansm}:{ansmm}')
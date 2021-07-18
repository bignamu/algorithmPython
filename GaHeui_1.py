import sys

N, M = map(int,sys.stdin.readline().rstrip().split())


filelist = []
extenlist = []

for _ in range(N):
    filelist.append(sys.stdin.readline().rstrip())

for _ in range(M):
    extenlist.append(sys.stdin.readline().rstrip())



# filelist = ['abc.jpeg', 'abc.jpg', 'foo.yolo', 'bar.cpp', 'bar.maltise']
# extenlist = ['jpg', 'cpp', 'maltise']

filelist.sort()
# print(filelist)


for i in range(len(filelist)-1):
    
    name, exten = filelist[i].split('.')
    back_name, back_exten = filelist[i+1].split('.')
    if exten not in extenlist and back_name == name:
        temp = filelist[i]
        filelist[i] = filelist[i+1]
        filelist[i+1] = temp
    elif exten not in extenlist and back_exten not in extenlist and back_name == name:
        if ord(exten)<ord(back_exten):
            temp = filelist[i]
            filelist[i] = filelist[i+1]
            filelist[i+1] = temp


for f in filelist:
    print(f)
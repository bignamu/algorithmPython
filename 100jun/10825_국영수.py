
N = int(input())

student = []
for _ in range(N):
    n,ko,en,ma = input().split()
    ko = int(ko)
    en = int(en)
    ma = int(ma)
    
    student.append([n,ko,en,ma])
    
student = sorted(student,key=lambda x:x[1])
print(student)


''' 

12
Junkyu 50 60 100
Sangkeun 80 60 50
Sunyoung 80 70 100
Soong 50 60 90
Haebin 50 60 100
Kangsoo 60 80 100
Donghyuk 80 60 100
Sei 70 70 70
Wonseob 70 70 90
Sanghyun 70 70 80
nsj 80 80 80
Taewhan 50 60 90

'''
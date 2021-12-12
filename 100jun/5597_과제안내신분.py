# https://www.acmicpc.net/problem/5597



student = [1]*31
student[0] = 0
for _ in range(28):
    student[int(input())] = 0


for i,v in enumerate(student):
    if v == 1:
        print(i)


# print(student)
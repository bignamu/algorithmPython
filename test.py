
a = [-1,-2,-3,-4]


a.sort()
last = a[-1]
print(a)

result = 0

for i in range(len(a)-2):
    minval = a[i]-a[i+1]
    print(minval)
    result -= minval
    print('result : ',result)    
    


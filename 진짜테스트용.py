print([0]*5)


s1 = 'hht'
s2 = 'hit'
print(list(set(s1)-set(s2)))
print(list(set(s2)-set(s1)))

s1list = [s11 for s11 in s1 if s11 in s2]

print(s1list)
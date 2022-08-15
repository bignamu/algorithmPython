_, _, *i = open(0)
for _ in (n := [-1, 1]+[0]*99):
    for l in i:
        a, b = map(int, l.split())
        n[b] = n[a] = n[a] | n[b]
print(sum(n))

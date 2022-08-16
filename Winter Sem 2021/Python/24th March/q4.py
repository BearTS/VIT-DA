l = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for i in range(len(l)):
    l[i] = l[i][:-1] + (100,)

print (l)

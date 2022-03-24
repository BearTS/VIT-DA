tup = ((1, 2, 3, 4, 5), (6, 7, 8, 9, 10, 7), (11, 12, 13, 14, 15))
l = []
for i in tup:
    sum = 0
    for j in i:
        sum = sum + j
    l.append(sum/len(i))
print(l)

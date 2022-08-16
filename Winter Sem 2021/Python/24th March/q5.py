li = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
sumOftup = []
for i in range(len(li)):
    sum = 0
    for j in range(len(li[i])):
        sum = sum + li[i][j]
    sumOftup.append(sum)

print(sumOftup)
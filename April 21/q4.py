# Anuj Parihar
# 21BBS0162
print('21BB0162 | Anuj Parihar')
print()

l1 = list()
l1 = [x for x in input("Enter any value for l1: ").split()]
l2 = list()
l2 = [x for x in input("Enter any value for l2: ").split()]
common = list()
 
for i in l1:
    for j in l2:
        if i == j:
            common.append(i)
 
common = set(common)
 
print("Common Items: ",common)
print("number of common items",len(common))
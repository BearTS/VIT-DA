# Name: Anuj Parihar
# RegNo: 21BBS0162

print('21BBS0162 Anuj Parihar')
telephone = {}
n = int(input("Enter the number of people: "))

for i in range(0,n):
    name = input("Enter the name: ")
    if name in telephone:
        telephone[name].append(input("Enter the number: "))
    else:
        number = input("Enter the number: ")
        telephone[name] = [number]

name = input("Enter the name to search: ")
print("Name", ":", "Mobile Numbers")
for key, value in telephone.items():
    if name.lower() in key.lower():
        print(key, ':', value)
    elif name.lower() in value[0].lower():
        print(key, ':', value)
    else: 
        pass
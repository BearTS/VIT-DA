# Python program to read a file line by line and store it into a list.
print("21BBS0162")
f = open("file.txt","r")
l = list()
for line in f:
    l.append(line)
print(l)
f.close()

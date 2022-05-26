# Python program to count the number of lines in a text file.
print("21BBS0162")
f = open("file.txt","r")
count = 0
for i in f:
    count += 1
print("Number of lines: ",count)
f.close()
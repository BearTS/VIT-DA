# Python program to remove newline characters from a file.
print("21BBS0162")
f = open("file.txt","r")
l = f.read()
for i in l:
    if i == "\n":
        l = l.replace(i,"")
f.close()
f = open("file.txt","w")
f.write(l)
f.close()
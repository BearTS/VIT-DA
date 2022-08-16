# program to print the largest word in a file
print("21BBS0162")
f = open("file.txt","r")
l = f.read()
l = l.split()
l.sort(key=len)
print(l[-1])
f.close()

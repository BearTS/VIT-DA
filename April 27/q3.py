# program to check whether two strings are anagram
def anagram(str1,str2):
    str1 = str1.replace(" ","")
    str2 = str2.replace(" ","")
    str1 = str1.lower()
    str2 = str2.lower()
    if len(str1) != len(str2):
        return False
    else:
        for i in str1:
            if i in str2:
                str2 = str2.replace(i,"",1)
            else:
                return False
        return True

print("21BBS0162")
string = input("Enter string 1: ")
string2 = input("Enter string 2: ")
if anagram(string,string2):
    print("Anagram")
else:
    print("Not anagram")

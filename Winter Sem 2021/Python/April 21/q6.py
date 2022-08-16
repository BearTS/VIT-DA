# Anuj Parihar
# 21BBS0162

print('21BBS0162 | Anuj Parihar')
print()
string = input("Enter a string: ")
key = 3

new_string = ""
for i in string:
    if i.isalpha():
        if i.isupper():
            new_string += chr((ord(i) - ord('A') + key) % 26 + ord('A'))
        else:
            new_string += chr((ord(i) - ord('a') + key) % 26 + ord('a'))
    else:
        new_string += i

print(new_string)
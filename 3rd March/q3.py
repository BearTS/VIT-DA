# Name: Bear
# RegNo: 21BBS0162
a = int(input("Enter a number: "))
if a % 7 == 0 and a % 9 == 0:
    print("Divisible by 7 and 9")
elif a % 7 == 0:
    print("Divisible by 7 only")
elif a % 9 == 0:
    print("Divisible by 9 only")
else:
    print("Not divisible by 7 or 9")

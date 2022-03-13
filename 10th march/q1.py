#print the total no of the digits in agiven number.
a = int(input("Enter a number: "))
b = a
sum = 0
while b > 0:
    sum = sum + 1
    b = b // 10
print("Total no of digits in", a, "is", sum)

# program to reverse a given number
a = int(input("Enter a number: "))
b = a
sum = 0
while b > 0:
    sum = sum * 10 + b % 10
    b = b // 10
print("Reverse of", a, "is", sum)

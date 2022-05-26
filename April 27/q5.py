# program to find the GCD of two numbers using recursion.
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

print("21BBS0162")
a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD = ",gcd(a,b))

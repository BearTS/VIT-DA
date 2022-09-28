def isPrime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

num = int(input("Enter a number: "))
if isPrime(num):
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
    print("Factorial of", num, "is", factorial(num))
# find nth root of a number
def nthroot(n, a):
    if n == 1:
        return a
    return a**(1/n)

num = int(input("Enter a number: "))
n = int(input("Enter n: "))
print(nthroot(n, num))
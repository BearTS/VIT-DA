# print n number of prime numbers 
def primeNumber(n):
    for i in range(2,n):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            print(i)
print("21BBS0162")
n = int(input("Enter n: "))
primeNumber(n)

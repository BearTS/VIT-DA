def sum(n):
    if n == 1:
        return 1
    return 1/n**2 + sum(n-1)

num = int(input("Enter a number: "))
print(sum(num))
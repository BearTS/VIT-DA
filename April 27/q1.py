# swap 2 variable 
def swap(a,b):
    a,b = b,a
    return a,b
print("21BBS0162")
a = input("Enter a: ")
b = input("Enter b: ")
a,b = swap(a,b)
print("a = ",a)
print("b = ",b)

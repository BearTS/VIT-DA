def area(a, b, h):
    return (a + b) * h / 2
a = int(input("Enter a: "))
h = int(input("Enter h: "))
b = int(input("Enter b: "))
print("Area of trapezium is", area(a, h, b))
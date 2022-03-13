
def grade(marks):    
    if marks >= 90:
        return 10
    elif marks >= 80:
        return 9
    elif marks >= 70:
        return 8
    elif marks >= 60:
        return 7
    elif marks >= 50:
        return 6
    elif marks >= 40:
        return 5
    else:
        return 0

a=int(input("Enter marks of first subject: "))
l=int(input("Enter number of credits of first subject: "))

b=int(input("Enter marks of second subject: "))
m=int(input("Enter number of credits of second subject: "))

c=int(input("Enter marks of third subject: "))
n=int(input("Enter number of credits of third subject: "))

d=int(input("Enter marks of fourth subject: "))        
o=int(input("Enter number of credits of fourth subject: "))

cgpa=(grade(a)*l+grade(b)*m+grade(c)*n+grade(d)*o)/(l+m+n+o)
print("CGPA: ",cgpa)
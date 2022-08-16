# program to print the multiplication table from 2 to n upto 10thterm.
# in list

n = int(input("Enter the number: "))

# list = [n*i for i in range(1, 11)] 
#
# if using list comprehension, the above code can be used instead of the below code:
list = []
for i in range(1,11):
    list.append(n*i)

print(list)


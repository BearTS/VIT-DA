# program to modify all elements in a list using list comprehension

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list = [i**3 if i%2 else i**2 for i in list]
print(list)
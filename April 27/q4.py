# a program to find the minimum and maximum element in the given list.
def minmax(list):
    min = list[0]
    max = list[0]
    for i in list:
        if i < min:
            min = i
        elif i > max:
            max = i
    return min,max

a = [1,2,3,4,5,6,7,8,9,10]
min, max = minmax(a)
print("21BBS0162")
print("Min: ",min)
print("Max: ",max)
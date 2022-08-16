# Anuj Parihar
# 21BBS0162
print('21BB0162 | Anuj Parihar')
print()

n = int(input("Enter number of items by son: "))
s=set()
for i in range(0,n): 
  s=s|{input("Enter son's item: ")}
   
n = 0
n = int(input("Enter number of items by daughter: "))
d=set()
for i in range(0,n):
  d=d|{input("Enter daughters item: ")}
 
print("common items: "+str(s&d)) 


print("Items of Son: "+str(s-d))
print("Items of Daugher: "+str(d-s))
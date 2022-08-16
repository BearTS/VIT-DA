# Anuj Parihar
# 21BBS0162
print('21BB0162 | Anuj Parihar')
print()

cities = {"Ratlam", "Mumbai", "Indore", "Vellore" ,"Bangalore", "Kanchi", "Jaipur", "Kolkata"}

s1 = ["Mumbai"]
s2 = ["Mumbai", "Kolkata"]
s3 = ["Ratlam", "Kanchi", "Indore"]

visit = set()
for city in s1:
    visit.add(city)

for city in s2:
    visit.add(city)

for city in s3:
    visit.add(city)

print("Visited cities: " + str(visit))
print("Cities not visited " + str(cities - visit))

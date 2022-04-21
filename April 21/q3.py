# Anuj Parihar
# 21BBS0162
print('21BB0162 | Anuj Parihar')
print()

students = [
{
  "Name": "Anuj", 
  "Register Number": "21BBS0162",
  "Marks": [80, 90, 55]
}, 
{
  "Name": "Tarran", 
  "Register Number": "21BBS0069",
  "Marks": [82, 92, 98]
}, 
{
  "Name": "Manan", 
  "Register Number": "21BBS0161",
  "Marks": [59, 69, 79]
}
]


for student in students:
  print(student["Name"] + ': ' + str(sum(student["Marks"]) / len(student["Marks"])))


# Name: Anuj Parihar
# RegNo: 21BBS0162
print('21BBS0162 Anuj Parihar')
dict_ = {'BATMAN': 'DC', 'IronMan': "MARVEL", "SpiderMan": "marvel", "Flash": "DC", "Doc Strange": "MARVEL"}
team = input("Enter the team name: ")
for key, value in dict_.items():
    if team.lower() == value.lower():
        print(key)
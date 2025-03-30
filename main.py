import csv

# file = open("Plik.txt")
# for line in file:
#     print(line, end=" ")
# file.close()
class Person:
    def __init__(self,name,surname,town):
        self.name = name
        self.surname = surname
        self.town = town

file =  open("names_towns.csv","r",encoding="utf-8")
csv_reader = csv.reader(file)
people = []
next(csv_reader)
for line in csv_reader:
    people.append(Person(line[0],line[1],line[2]))

print(len(people))

for i in range(len(people)):
    print("Pan/Pani " + people[i].name + " " + people[i].surname  +" mieszka w "+ people[i].town )
file.close()
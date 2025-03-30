import csv

# file = open("Plik.txt")
# for line in file:
#     print(line, end=" ")
# file.close()

file =  open("names_towns.csv","r",encoding="utf-8")
csv_reader = csv.reader(file)
names = []
surnames = []
towns = []
next(csv_reader)
for line in csv_reader:
    names.append(line[0])
    surnames.append(line[1])
    towns.append(line[2])

print(len(names))

for i in range(len(names)):
    print("Pan/Pani " + names[i] + " " + surnames[i]  +" mieszka w "+ towns[i] )
file.close()
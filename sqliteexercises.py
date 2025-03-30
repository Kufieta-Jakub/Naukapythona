import sqlite3
connection = sqlite3.connect("moja_baza_danych")

cursor = connection.cursor()


cursor.execute('''
Create TABLE IF NOT EXISTS persons(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    surname TEXT,
    town TEXT
)
''')

cursor.execute('''
INSERT INTO persons (name,surname,town) 
    VALUES (?,?,?)
''',("Iwona","Anielewicz","Gdańsk"))

connection.commit()

cursor.execute('''
SELECT * FROM persons
''')
rows = cursor.fetchall()
for row in rows:
    print(row)

connection.close()
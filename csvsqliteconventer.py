import csv
import sqlite3


def is_number(value: str) -> bool:
    try:
        float(value)
        return True
    except ValueError:
        return False


BAZA_DANYCH = "nowa_baza.db"
FILE = open("names_towns.csv", "r", encoding="UTF-8")
HEADERSTOFILE = "id INTEGER PRIMARY KEY AUTOINCREMENT, "
HEADERSTOINSERT = ""
FIRSTVALUES = ""
connection = sqlite3.connect(BAZA_DANYCH)
cursor = connection.cursor()
headersTab = []

print("Witaj w konwerterze pliku csv-sqlite co chcesz zrobić:")
print("1.Konwertuj plik csv do bazy/tabeli")
print("2.Konwertuj baze/tabele do pliku csv")
choice = input()

if choice == "1":
    print("Podaj nazwę tabeli dla danych:")
    tableName = input()
    csvreader = csv.reader(FILE)
    headers = next(csvreader)
    values = next(csvreader)


    for header in headers:
        headersTab.append(header)
        HEADERSTOINSERT += header + ", "
    HEADERSTOINSERT = HEADERSTOINSERT[:-2]

    print(HEADERSTOINSERT)


    for index, value in enumerate(values):
        if is_number(value):
            HEADERSTOFILE += headersTab[index] + " INTEGER, "
            FIRSTVALUES += value + ", "
        else:
            HEADERSTOFILE += headersTab[index] + " TEXT, "
            FIRSTVALUES += f"'{value}'" + ", "

    HEADERSTOFILE = HEADERSTOFILE[:-2]
    FIRSTVALUES = FIRSTVALUES[:-2]


    cursor.execute(f'''
    CREATE TABLE IF NOT EXISTS {tableName} (
        {HEADERSTOFILE}
    )
    ''')

    cursor.execute(f'''
        INSERT INTO {tableName} ({HEADERSTOINSERT}) VALUES ({FIRSTVALUES})
    ''')

    for line in csvreader:
        values = ""
        for value in line:
            if is_number(value):
                values += value + ", "
            else:
                values += f"'{value}', "

        values = values[:-2]

        cursor.execute(f'''
            INSERT INTO {tableName} ({HEADERSTOINSERT}) VALUES ({values})
        ''')

    connection.commit()

    cursor.execute(f'''
    SELECT * FROM {tableName}
    ''')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    connection.close()


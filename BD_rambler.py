import sqlite3
import ram

# Подключение к БД.
conn = sqlite3.connect('rambler.db')
cursor = conn.cursor()

# cписок групп в которых нужно узнать сколько подписчиком в ней
id = ['rambler', 'ramblermail', 'horoscopesrambler', 'championat',
      'championat.auto', 'championat_cybersport', 'livejournal', 'afisha']
# Токен для подключения к API VK
toc = ''

data = ram.namder(id, toc)


def bd_rambler(data):
    for tabl in range(len(data)):
        g = []
        name = data[tabl][0].replace('.', '_')
        g.append(name)
        count = data[tabl][1]
        g.append(count)
        try:
            # Создание таблицы
            cursor.execute(
                """CREATE TABLE table_ram (id INTEGER PRIMARY KEY AUTOINCREMENT, name_grup TEXT, count INT, date REAL NOT NULL) """)
            cursor.execute("""INSERT INTO table_ram (name_grup, count, date) VALUES ( ?, ?,CURRENT_DATE)""", g)
        except:
            cursor.execute("""INSERT INTO table_ram (name_grup, count, date) VALUES ( ?, ?,CURRENT_DATE)""", g)

    cursor.execute("""SELECT * FROM table_ram """)
    gf = cursor.fetchall()
    for res in range(len(gf)):
        print(gf[res])


bd_rambler(data)

conn.commit()
cursor.close()
conn.close()

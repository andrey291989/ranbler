import sqlite3
import ram
import time

# cписок групп в которых нужно узнать сколько подписчиком в ней.
id = ['rambler', 'ramblermail', 'horoscopesrambler', 'championat',
      'championat.auto', 'championat_cybersport', 'livejournal', 'afisha']

# Токен для подключения к API VK (безательный аргумент)
toc = ''

# Время с какой переодичностью нужно собирать данные (в секундах).
t = 2

data = ram.namder(id, toc)


def bd_rambler(data, t):
    # Подключение к БД.
    conn = sqlite3.connect('rambler.db')
    cursor = conn.cursor()
    print('')
    print('Новый день, новые данные!')
    for tabl in range(len(data)):
        g = []
        name = data[tabl][0].replace('.', '_')
        g.append(name)
        count = data[tabl][1]
        g.append(count)

        try:
            # Создание таблицы.
            cursor.execute(
                """CREATE TABLE table_ram (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                name_grup TEXT, count INT, date REAL NOT NULL) """)
        except:
            pass

        cursor.execute("""INSERT INTO table_ram (name_grup, count, date) 
        VALUES ( ?, ?, CURRENT_TIMESTAMP)""", g)

    cursor.execute("""SELECT * FROM table_ram """)
    gf = cursor.fetchall()
    for res in range(len(gf)):
        print(gf[res])

    # Коммит данных и перкращение работы с БД.
    conn.commit()
    cursor.close()
    conn.close()

    # loop событий
    time.sleep(t)
    bd_rambler(data, t)


if __name__ == '__main__':
    bd_rambler(data, t)

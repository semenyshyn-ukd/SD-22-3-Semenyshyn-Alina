import sqlite3
conn = sqlite3.connect("trains.db")
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS train_routes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        train_number TEXT NOT NULL,
        departure TEXT NOT NULL,
        destination TEXT NOT NULL,
        departure_time TEXT NOT NULL,
        arrival_time TEXT NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS train_cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        train_number TEXT NOT NULL,
        car_type TEXT NOT NULL,
        seat_count INTEGER,
        FOREIGN KEY (train_number) REFERENCES train_routes (train_number)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS train_tickets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        train_number TEXT NOT NULL,
        car_id INTEGER NOT NULL,
        passenger_name TEXT NOT NULL,
        seat_number INTEGER NOT NULL,
        price REAL NOT NULL,
        FOREIGN KEY (train_number) REFERENCES train_routes (train_number),
        FOREIGN KEY (car_id) REFERENCES train_cars (id)
    )
''')

cursor.executemany('''
    INSERT INTO train_routes (train_number, departure, destination, departure_time, arrival_time) VALUES (?, ?, ?, ?, ?)
''', [
    ("IC125", "Київ", "Львів", "08:00", "14:30"),
    ("RE256", "Львів", "Одеса", "10:15", "22:45"),
    ("NV341", "Харків", "Дніпро", "07:30", "10:00"),
    ("IC789", "Одеса", "Київ", "16:00", "23:15"),
    ("RE654", "Дніпро", "Львів", "12:45", "23:30")
])

cursor.executemany('''
    INSERT INTO train_cars (train_number, car_type, seat_count) VALUES (?, ?, ?)
''', [
    ("IC125", "Плацкарт", 54),
    ("IC125", "Купе", 36),
    ("RE256", "СВ", 18),
    ("NV341", "Плацкарт", 54),
    ("IC789", "Купе", 36)
])

cursor.executemany('''
    INSERT INTO train_tickets (train_number, car_id, passenger_name, seat_number, price) VALUES (?, ?, ?, ?, ?)
''', [
    ("IC125", 1, "Іван Петренко", 12, 450.00),
    ("IC125", 2, "Марія Іваненко", 8, 600.00),
    ("RE256", 3, "Олег Коваленко", 5, 1200.00),
    ("NV341", 4, "Анна Савченко", 27, 350.00),
    ("IC789", 5, "Петро Бондар", 14, 700.00)
])

cursor.execute("SELECT * FROM train_routes")
rows = cursor.fetchall()

print("\nRoutes")
print(" ")
for el in rows:
    print(f'\nНомер маршруту: {el[0]}'
          f'\nID: {el[1]}'
          f'\nМісце відправлення: {el[2]}'
          f'\nМісце прибуття: {el[3]}'
          f'\nЧас відправлення: {el[4]}'
          f'\nЧас прибуття: {el[5]}')

cursor.execute("SELECT * FROM train_cars")
rows = cursor.fetchall()

print("\nCars")
for el in rows:
    for el in rows:
        print(f'\nНомер транспорту: {el[0]}'
              f'\nID: {el[1]}'
              f'\nВид транспорту: {el[2]}'
              f'\nК-сть сидінь: {el[3]}')

cursor.execute("SELECT * FROM train_tickets")
rows = cursor.fetchall()

print("\nTicket")
for el in rows:
    print(f'\nНомер маршруту: {el[0]}'
          f'\nID: {el[1]}'
          f'\nПІБ: {el[2]}'
          f'\nМісце: {el[3]}'
          f'\nЦіна: {el[4]}')

conn.commit()

conn.close()
# Приложение СДАЧА В АРЕНДУ ТОРГОВЫХ ПЛОЩАДЕЙ для некоторой
# организации. БД должна содержать таблицу Торговая точка со следующей структурой
# записи: этаж, площадь, наличие кондиционера и стоимость аренды в день.

import _sqlite3 as sq
from data_trade_area import trade_area

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS trade")
    cur.execute("""CREATE TABLE IF NOT EXISTS trade (
    trade_id INTEGER PRIMARY KEY AUTOINCREMENT,
    stage INTEGER NOT NULL, 
    square INTEGER NOT NULL, 
    conditioner BOOLEAN NOT NULL, 
    price INTEGER
    )""")

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.executemany("INSERT INTO trade VALUES (?, ?, ?, ?, ?)", trade_area)

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM trade")
    result = cur.fetchall()
    print(result)

# SELECT SEARCH
with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM trade WHERE conditioner")
    result = cur.fetchall()
    print(result)

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM trade WHERE price > 2000 and conditioner = false")
    result = cur.fetchall()
    print(result)

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("SELECT * FROM trade WHERE square < 100 and conditioner and price >= 2000")
    result = cur.fetchall()
    print(f'{result}\n')

# UPDATE
with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE trade SET price = 2000 WHERE price < 2000")
    result = cur.fetchall()
    print(result)

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE trade SET conditioner = true WHERE square > 100")
    result = cur.fetchall()
    print(result)

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("UPDATE trade SET price = 2300 WHERE stage < 7 ")
    result = cur.fetchall()
    print(result)

# DELETE
with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM trade WHERE price > 2700")
    result = cur.fetchall()
    print(result)

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM trade WHERE square < 90")
    result = cur.fetchall()
    print(result)

with sq.connect('trade.db') as con:
    cur = con.cursor()
    cur.execute("DELETE FROM trade WHERE price < 2300 ")
    result = cur.fetchall()
    print(result)

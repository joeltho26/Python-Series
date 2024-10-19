import sqlite3

conn = sqlite3.connect('./SQLite/example.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS stocks(date text, trans text, symbol text, qty real, price real)''')
cursor.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

conn.commit()

sql_query = """SELECT DISTINCT * FROM stocks;"""
cursor.execute(sql_query)
result = cursor.fetchall()
print(result)

conn.close()

import pymysql

#CONNECTION
my_db = pymysql.connect(host='localhost',user='root', port=3306,password='Windows8*Olya',database='TEST')
my_cursor = my_db.cursor()

# CREATE DATABASE
my_cursor.execute("CREATE DATABASE mydatabase")

# SHOW DATABASE
my_cursor.execute("SHOW DATABASES")
for i in my_cursor:
    print(i)

# CREATE TABLE
my_cursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# SHOW TABLE
my_cursor.execute("SHOW TABLES")
for i in my_cursor:
    print(i)

# ALTER TABLE
my_cursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
my_db.commit()

#INSERT ONE RECORD
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
my_cursor.execute(sql, val)
my_db.commit()

#INSERT MULTIPLE RECORDS 
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

my_cursor.executemany(sql, val)
my_db.commit()
print(my_cursor.rowcount, "was inserted.")
print("last record inserted, ID:", my_cursor.lastrowid)

# SELECT RECORDS
my_cursor.execute("SELECT * FROM customers")
myresult = my_cursor.fetchall()
for x in myresult:
    print(x)

# SELECT ONE RECORDS
my_cursor.execute("SELECT * FROM customers")
myresult = my_cursor.fetchone()
for x in myresult:
    print(x)

# FILTER RECORD AND WILDCARD
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
my_cursor.execute(sql)
myresult = my_cursor.fetchall()
for x in myresult:
    print(x)
  
# ORDER RECORDS  
sql = "SELECT * FROM customers ORDER BY name DESC"
my_cursor.execute(sql)
myresult = my_cursor.fetchall()
for x in myresult:
    print(x)

# DELETE RECORDS
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
my_cursor.execute(sql)
my_db.commit()
print(my_cursor.rowcount, "record(s) deleted")

# DROP TABLE
sql = "DROP TABLE IF EXISTS customers"
my_cursor.execute(sql)

# UPDATE RECORDS
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
my_cursor.execute(sql)
my_db.commit()
print(my_cursor.rowcount, "record(s) affected")

# LIMIT RECORDS AND OFFSET
my_cursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
myresult = my_cursor.fetchall()
for x in myresult:
    print(x)

#JOIN TABLE
sql = "SELECT \
  users.name AS user, \
  products.name AS favorite \
  FROM users \
  INNER JOIN products ON users.fav = products.id"

my_cursor.execute(sql)
myresult = my_cursor.fetchall()
for x in myresult:
    print(x)
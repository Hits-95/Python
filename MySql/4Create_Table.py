#create Table...
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="Hitesh",
  password="Online...",
  database="Py_Test"  
)
mycursor = mydb.cursor()

#mycursor.execute("CREATE TABLE customers(name text, address text)")
#alter table cmd...
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#check if table exists...
mycursor.execute("SHOW TABLES")
for x in mycursor:
  print(x)

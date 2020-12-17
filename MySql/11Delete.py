#delete...
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Hitesh",
  password="Online...",
  database="py_test"
)

mycursor = mydb.cursor()

sql = "DELETE FROM customers WHERE address = 'tehare'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

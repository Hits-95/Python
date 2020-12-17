#Update...
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Hitesh",
  password="Online...",
  database="py_test"
)

mycursor = mydb.cursor()

sql = "UPDATE customers SET address = 'nsk' WHERE address = 'pachore'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

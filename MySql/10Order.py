#Order....
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Hitesh",
  password="Online...",
  database="py_test"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name DESC"
#sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

#check if database is exists...
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Hitesh",
  password="Online...",
  database="Py_Test"  #optional parra  to use direct connect to dbs
)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)

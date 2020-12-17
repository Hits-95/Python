#Select i.e fetch records...
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "Hitesh",
    password = "Online...",
    database = "Py_Test"
    )
mycursor = mydb.cursor()
mycursor.execute("select * from customers")

result = mycursor.fetchall()

for x in result:
    print(x)


#select colm vs....
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "Hitesh",
    password = "Online...",
    database = "py_test"
)

mycursor = mydb.cursor()
mycursor.execute("select id,name from customers;")
result = mycursor.fetchall()
for x in result:
    print(x)

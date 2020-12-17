#where
import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "Hitesh",
    password = "Online...",
    database = "py_test"
)
mycursor = mydb.cursor()

#sql = "SELECT * FROM customers WHERE address ='mugse'"

sql = "SELECT * FROM customers WHERE address LIKE '%re%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

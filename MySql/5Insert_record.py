#insert record...
import mysql.connector

mydb = mysql.connector.connect(
      host = "localhost",
      user = "Hitesh",
      password="Online...",
      database="Py_Test"  
    )
mycursor = mydb.cursor()
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
name = input("Enter Name : ")
addr = input("Enter address : ")
val = (name, addr)

mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted...")

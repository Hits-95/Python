#insert many records....
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "Hitesh",
    password = "Online...",
    database = "Py_Test"
    )
mycursor = mydb.cursor()


sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

val = [
    ('pd','tehare'),
    ('komal','jalgaon'),
    ('vrushali','mugse'),
    ('vishakha','malegaon'),
    ('pooja','kavlane'),
    ('nikita','pachore')
    ]
mycursor.executemany(sql,val)
mydb.commit()

print(mycursor.rowcount,"was inserted...")
print("last inserted record , ID:", mycursor.lastrowid)


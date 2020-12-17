#create Database Py_Test...

import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "Hitesh",
    password = "Online..."
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Py_Test")

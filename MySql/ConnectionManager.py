#connection manager module
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "Hitesh",
    password = "Online...",
    database = "Py_Test"
    )

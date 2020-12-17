# Test MySql Connection....

import mysql.connector as con

mydb = con.connect(
  host="localhost",
  user="root",
  password=""
)

print(mydb)


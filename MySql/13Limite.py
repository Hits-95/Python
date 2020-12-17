#limit...
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="Hitesh",
  password="Online...",
  database="py_test"
)

mycursor = mydb.cursor()

#sql = " select * from Customers limit 5;"

"""If you want to return five records,
starting from the third record, you can use the "OFFSET" keyword:
"""

sql = "SELECT * FROM customers LIMIT 5 OFFSET 2"

mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
    print(x)

'''To find only the documents where the "address" field starts with the letter "S",
use the regular expression {"$regex": "^S"}:'''

import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']
qry = { "address": { "$regex": "^P" } }
result = mycoln.find(qry)
for x in result:
    print(x)



    

'''To find only the documents where the "address" field starts with the letter "S",
use the regular expression {"$regex": "^S"}:'''

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']
qry = { "address": { "$regex": "^P" } }
result = mycoln.find(qry)
for x in result:
    print(x)



    

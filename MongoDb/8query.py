#display selected colms....
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']
qry = { "address": "Tehare"}
result = mycoln.find(qry)
for x in result:
    print(x)



    

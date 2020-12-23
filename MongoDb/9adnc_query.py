#display selected colms....
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']
qry = { "address": { "$gt": "S" } }
result = mycoln.find(qry)
for x in result:
    print(x)



    

#limite...
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']

for x in mycoln.find().limit(4):
    print(x)
    

#sort ascending...
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']

result = mycoln.find().sort("name",-1)
for x in result:
    print(x)



    
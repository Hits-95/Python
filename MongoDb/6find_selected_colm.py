#display selected colms....
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']
result = mycoln.find({},{"_id":0,"name":1,"address":1})
for x in result:
    print(x)



    

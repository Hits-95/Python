#display selected colms....
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online1@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']
result = mycoln.find({},{"_id":0,"name":1,"address":1})
for x in result:
    print(x)



    

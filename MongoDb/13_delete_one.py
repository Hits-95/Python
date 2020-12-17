#DElete one  Record...
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']
qry = {"name":"Hitesh"}
#for delete all records...
#mycoln.delete_many({})
print(mycoln.delete_one(qry))



    

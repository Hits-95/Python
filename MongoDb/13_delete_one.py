#DElete one  Record...
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']
qry = {"name":"Hitesh"}
#for delete all records...
#mycoln.delete_many({})
print(mycoln.delete_one(qry))



    

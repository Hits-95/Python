'''Delete all documents were the name starts with the letter S:'''
#DElete many  Record...
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']

qry = {"name":{"$regex" : "^s"}}

result = mycoln.delete_many(qry)

print(result.deleted_count, "documents deleted.")



    

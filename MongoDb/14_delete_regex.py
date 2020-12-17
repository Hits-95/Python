'''Delete all documents were the name starts with the letter S:'''
#DElete many  Record...
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']

qry = {"name":{"$regex" : "^s"}}

result = mycoln.delete_many(qry)

print(result.deleted_count, "documents deleted.")



    

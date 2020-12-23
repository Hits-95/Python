#create collection l.e table...
'''Important: In MongoDB, a collection is not created until it gets content!'''
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/<dbname>?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']
mydict = {"name":"Shruti ","address":"dule"}
print(mycoln.count_documents({}))
result = mycoln.insert_one(mydict)
print(result)
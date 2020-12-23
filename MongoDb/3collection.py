#create collection l.e table...
'''Important: In MongoDB, a collection is not created until it gets content!'''
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")
mydb = myclient['py_test']
mycoln = mydb['customer']
print(mydb.list_collection_names())

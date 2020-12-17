#create collection l.e table...
'''Important: In MongoDB, a collection is not created until it gets content!'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']
print(mydb.list_collection_names())

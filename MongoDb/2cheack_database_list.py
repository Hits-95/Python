#cheack database list
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

print(myclient.list_database_names())

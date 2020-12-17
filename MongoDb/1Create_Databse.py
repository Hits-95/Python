import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient['Py_test']
print(mydb)

# database created!

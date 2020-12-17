#display one records...
#find_one() method returns the first occurrence in the selection.
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']

x = mycoln.find_one()

print(x)



    

#display one records...
#find_one() method returns the first occurrence in the selection.
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']

x = mycoln.find_one()

print(x)



    

#update....
'''Change the address from "Tehare" to "at tehare malegaon":'''
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://Hitesh:online@cluster0.w9ui5.mongodb.net/py_test?retryWrites=true&w=majority")

mydb = myclient['py_test']
mycoln = mydb['customer']

condn_qry = { "address": "Tehare" }
set_qry = { "$set": { "address": "at tehare malegaon" } }

mycoln.update_one(condn_qry, set_qry)
for x in mycoln.find():
    print(x)
    

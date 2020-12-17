#update....
'''Change the address from "Tehare" to "at tehare malegaon":'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']

condn_qry = { "address": "Tehare" }
set_qry = { "$set": { "address": "at tehare malegaon" } }

mycoln.update_one(condn_qry, set_qry)
for x in mycoln.find():
    print(x)
    

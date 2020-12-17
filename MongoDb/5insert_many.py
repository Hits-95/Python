#insert many record
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017")
mydb = myclient['py_test']
mycoln = mydb['customer']
mylist = [{"_id" : 1, "name" : "sakshi", "address" : "pimplgaon"},
          {"_id" : 2, "name" : "Komal", "address" : "Jalgaon"},
          {"_id" : 3, "name" : "Pd", "address" : "Tehare"},
          {"_id" : 4, "name" : "Vrushali", "address" : "Mugse"},
          {"_id" : 5, "name" : "Pooja", "address" : "Kavlane"},
          {"_id" : 6, "name" : "Nikita", "address" : "Pachore"},
          {"_id" : 7, "name" : "Vishaka", "address" : "Malegaon"},
          {"_id" : 8, "name" : "Ganesh"," address" : "Nashik"}
    ]
x = mycoln.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

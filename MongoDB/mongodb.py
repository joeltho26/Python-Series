#Check the env for MongoDB and use the correct one for it to work
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://joeljoseph26:Windows8Olya@clustertestjoel.df6afsx.mongodb.net/"
myclient = MongoClient(uri)

try:
    myclient.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
# CREATE DATABASE AND TABLE
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
print(myclient.list_database_names())

# INSERT RECORDS
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)
print(x.inserted_id)

# INSERT MANY
mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)

# INSERT MANY with specific IDs
mylist = [
    { "_id": 1, "name": "John", "address": "Highway 37"},
    { "_id": 2, "name": "Peter", "address": "Lowstreet 27"},
    { "_id": 3, "name": "Amy", "address": "Apple st 652"},
    { "_id": 4, "name": "Hannah", "address": "Mountain 21"},
    { "_id": 5, "name": "Michael", "address": "Valley 345"},
    { "_id": 6, "name": "Sandy", "address": "Ocean blvd 2"},
    { "_id": 7, "name": "Betty", "address": "Green Grass 1"},
    { "_id": 8, "name": "Richard", "address": "Sky st 331"},
    { "_id": 9, "name": "Susan", "address": "One way 98"},
    { "_id": 10, "name": "Vicky", "address": "Yellow Garden 2"},
    { "_id": 11, "name": "Ben", "address": "Park Lane 38"},
    { "_id": 12, "name": "William", "address": "Central st 954"},
    { "_id": 13, "name": "Chuck", "address": "Main Road 989"},
    { "_id": 14, "name": "Viola", "address": "Sideway 1633"}
]

x = mycol.insert_many(mylist)
print(x.inserted_ids)

# FIND ONE RECORD
x = mycol.find_one()
print(x)

#FIND ALL RECORDS
for x in mycol.find():
    print(x)

#FIND RECORDS AND RETURN ONLY NAME AND ADDRESS NOT ID
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
    print(x)

#QUERY RECORDS
myquery = { "address": { "$gt": "S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

#QUERY RECORDS WITH REGULAR EXPRESSIONS
myquery = { "address": { "$regex": "^S" } }
mydoc = mycol.find(myquery)
for x in mydoc:
    print(x)

# SORTING RECORDS
mydoc = mycol.find().sort("name", -1)
for x in mydoc:
    print(x)

# DELETE RECORDS
myquery = { "address": "Mountain 21" }
mycol.delete_one(myquery)

# DELETE MULTIPLE RECORDS
myquery = { "address": {"$regex": "^S"} }
x = mycol.delete_many(myquery)
print(x.deleted_count, " documents deleted.")

#DELETE ALL RECORDS
x = mycol.delete_many({})
print(x.deleted_count, " documents deleted.")

#UPDATE ONE RECORD
myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update_one(myquery, newvalues)
for x in mycol.find():
    print(x)

# UPDATE MANY RECORDS
myquery = { "address": { "$regex": "^S" } }
newvalues = { "$set": { "name": "Minnie" } }
x = mycol.update_many(myquery, newvalues)
print(x.modified_count, "documents updated.")

# LIMIT RECORDS
myresult = mycol.find().limit(5)
for x in myresult:
    print(x)
    
# DROP COLLECTION
mycol.drop()
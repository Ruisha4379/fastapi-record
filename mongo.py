"""
Test insert data into mongoDB locally
Testing based on the ref: https://www.geeksforgeeks.org/python-mongodb-insert_one-query/
"""
from pymongo import MongoClient

client = MongoClient(host="localhost", port = 27017) #db = "hrms",
#client = MongoClient("mongodb://localhost:27017/")
# database
db = client["GFG"]

# Created or Switched to collection
collection = db["Student"]
 
# Creating Dictionary of records to be
# inserted
records = {
    "record1": { "_id": 6,
    "name": "Anshul",
    "Roll No": "1006",
    "Branch": "CSE"},
 
    "record2": { "_id": 7,
    "name": "Abhinav",
    "Roll No": "1007",
    "Branch": "ME"}
}
  
# Inserting the records in the collection
# by using collection.insert_one()
for record in records.values():
    collection.insert_one(record)

cursor=collection.find()
for record in cursor:
    print(record)
# How to varify the data has been inserted into the db created?
# Step 1: type `mongo` at the terminal to enter the mongo shell
# Step 2: type `show dbs` to check whether the db is created successfully
# Step 3: type `use GFG` to enter the db created
# Step 4: type `db.Student.find()` to see the content of the collection 

"""
POST data to API endpoint meanwhile save it to MongDB
"""
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
import uvicorn
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

client = MongoClient()
db = "vpp_data"
col = "create_vpp" # database collection
# Message class defined in Pydantic
class VPP(BaseModel):
    name: str
    vpp_id: str
    status: str
    market_id: str
    market_type: str
# Instantiate the FastAPI
app = FastAPI()

@app.post("/data/vpptree", status_code=status.HTTP_201_CREATED)
def post_vpp(create_vpp: VPP):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_col = client[db][col]
        insert_result = msg_col.insert_one(create_vpp.dict())
        msg_content = VPP(**create_vpp.dict())
        ack = insert_result.acknowledged
        #print (msg_col)
        print(insert_result)
        print(msg_content)
        
        for doc in msg_col.find():
            pp.pprint(doc) # pretty print the returned documents
        return {"Data insertion": ack}
        
if __name__ == '__main__':
    #it will run on port 8000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')
    
# How to varify the data input from the POST endpoint is successfully insert into the mongoDB:     
# Step 1: Tyep `$ ./mongod` at the root path
# Step 2: Type `mongto` in the environment path to run in the mongo shell 
# Step 3: Type `show dbs` to see all the db created in the mongo shell
# Step 4: Type `use sw_data` to enter the db created
# Step 5: Type 'db.messages.find()' to check the content of the collection inserted

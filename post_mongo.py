"""
POST some data to the endpoint and meanwhile save it into mongoDB.
"""
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from typing import List
import uvicorn
import json

client = MongoClient()

DB = "sw_data"
MSG_COLLECTION = "messages"
# Message class defined in Pydantic
class Message(BaseModel):
    channel: str
    author: str
    text: str
# Instantiate the FastAPI
app = FastAPI()

@app.post("/post_message", status_code=status.HTTP_201_CREATED)
def post_message(message: Message):
    """Post a new message to the specified channel."""
    with MongoClient() as client:
        msg_collection = client[DB][MSG_COLLECTION]
        insert_result = msg_collection.insert_one(message.dict())
        msg_content = Message(**message.dict())
        ack = insert_result.acknowledged
        print (msg_collection)
        print(insert_result)
        print(msg_content)
        return {"Data insertion": ack}
        
if __name__ == '__main__':
    #it will run on port 3000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')
    
# Type `mongto` in the environment
# Type `show dbs` to see all the db created
# To show detail content of a collection: https://stackoverflow.com/questions/24985684/mongodb-show-all-contents-from-all-collections 

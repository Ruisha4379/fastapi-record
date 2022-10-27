Tasks:
1. Create the POST endpoint to receive data sent from UI
2. Meanwhile get the json data sent from UI
2. Save the json data to MongDB
"""
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from typing import Optional, List, Dict, Union
import uvicorn
import json
import asyncio
#from json import JSONDecodeError
#import requests
#from enum import Enum
import pprint
pp = pprint.PrettyPrinter(indent=4)

app = FastAPI()

client = MongoClient()
db = "vpp_data"
col = "create_vpp_R1" # database collection

class VPP(BaseModel):
    Name: str
    VPP_ID: str
    Market_Type: str#['FR', 'DR', 'Reserve', 'Energy']
    Control_Area: str#['CAISO','PJM', 'Singapore PSO', 'Chubu']
    Communication_Protocol: str#['Open ADR', 'Echonetlite', 'IEC 104']
    Flex_Up_Cost: str
    Flex_Down_Cost: str
    Flex_Up_Capacity: str # calculated from the site capacity
    Flex_Down_Capacity: str # calculated from the site capacity
    Description: str
    Sites: str # Need to be linked with sites mongodb
    
@app.post("/data/vpptree")
async def get_data(request: Request):
    body = await request.json()
    # json.loads take a string as input and returns a dictionary as output.
    #obj = json.loads(body)
    print(body)
    print(type(body)) # type of obj is dict
    
    with MongoClient() as client:
        msg_col = client[db][col]
        msg_content = VPP(**body)
        insert_result = msg_col.insert_one(msg_content.dict())
        
        for doc in msg_col.find():
            pp.pprint(doc) # pretty print the returned documents

    return body

if __name__ == '__main__':
#     #it will run on port 8000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')

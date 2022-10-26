"""

Tasks:
1. Create the POST endpoint to receive data sent from UI
2. Meanwhile get the json data sent from UI
2. Save the json data to MongDB (To be continued)
"""
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from typing import Optional, List, Dict, Union
import uvicorn
import json
from json import JSONDecodeError
import requests
from enum import Enum
import pprint
pp = pprint.PrettyPrinter(indent=4)

app = FastAPI()

# @app.post("/data/vpptree", status_code=status.HTTP_201_CREATED)
# def post_vpp():
    
#     return 'create endpoint successful'

@app.post("/data/vpptree")
async def get_data(request: Request):
    #try:
        #payload_as_json = await request.json()
    body = await request.body()
    obj = json.loads(body)
    #request = Request(**obj)
    message = "Success"
    #pp.pprint(body)
    print(int(obj['Flex_Up_Cost ($/MWh)'])*2.3)
    #except JSONDecodeError:
        #payload_as_json = None
        #message = "Received data is not a valid JSON"
    #return {"message": message, "received_data_as_json": body}
    return obj

if __name__ == '__main__':
#     #it will run on port 8000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')

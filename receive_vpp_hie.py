"""
Date: 2022-10-31
Tasks:
1. Create the POST endpoint to receive data sent from UI
2. Meanwhile get the json data sent from UI
2. Save the json data to MongDB
"""

from pymongo import MongoClient
from mongoengine import connect
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from models_hie import Vpp_metadata, Sites_metadata
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
client   = MongoClient()
#db       = "vpp_data"
col_vpp  = "vpp_metadata" # for vpp
col_site = "sites_metadata" # for list of sites

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
    
class Sites(BaseModel):  
    Name:str
    Site_ID: str
    Site_address:str
    Assigned_VPP: str
    Description: str
    Market_resource: str
    
@app.post("/create_vpp")
async def get_created_vpp(request: Request):
    body = await request.json()
    #json.loads take a string as input and returns a dictionary as output.
    #obj = json.loads(body)
    print(body)
    #Extract the vpp name from the data send by create vpp form UI
    db = body['Name']
    print("VPP name extracted is",db)
    with MongoClient() as client:
        msg_col = client[db][col_vpp]
        msg_content = VPP(**body)
        print('msg_col type is:', type(msg_col))
        insert_result = msg_col.insert_one(msg_content.dict())
        #Print the lastes inserted collection:
        print('The latest inserted collection is')
        #List the collection in msg_col sorted based on vpp_name
        for doc in msg_col.find().sort('Name',-1).limit(1):
            pp.pprint(doc) # pretty print the returned documents
        
    return body
    
@app.post("/create_sites")
async def get_created_sites(request: Request):
    body_site = await request.json()
    print(body_site)
    print(type(body_site)) # type of obj is dict
    site_rename = body_site['Name']
    site_vpp    = body_site['Assigned_VPP']
    print(site_vpp)
    with MongoClient() as client:
        msg_col = client[site_vpp][col_site]
        msg_content = Sites(**body_site)
        insert_result = msg_col.insert_one(msg_content.dict())
        
        for doc in msg_col.find().sort('Name',-1).limit(1):
            pp.pprint(doc)
    return body_site

connect(db = "VppDemo1", host="localhost", port = 27017)
@app.get("/get_vpp")
def get_vpp():
    vpp = json.loads(Vpp_metadata.objects().to_json()) # return all the docs in db collection
    #vpp = Create_vpp.objects()
    pp.pprint(vpp)
    print(type(vpp)) # print the types of var
    return {"VPP created":  vpp} # retun to the client
    
@app.get("/get_sites")
def get_sites():
    sites = json.loads(Sites_metadata.objects().to_json()) # return all the docs in db collection
    pp.pprint(sites)
    print(type(sites)) # print the types of var
    return {"Sites created":  sites} # retun to the client

if __name__ == '__main__':
#     #it will run on port 8000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')
    

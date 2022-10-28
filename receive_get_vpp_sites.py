"""
Tasks:
1. Create the POST endpoints to receive data sent from UI for creating of VPP and one site
2. Meanwhile get the json data sent from UI
3. Save the vreate_vpp and create_site json data to MongDB
4. Get the vpp and site created data from the mongDB db created (note the models.py is needed)
"""
# Illustrates basic usage of FastAPI w/ MongoDB
from pymongo import MongoClient
from mongoengine import connect
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from models import Create_vpp
from models import Create_sites
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
connect(db = "vpp_data", host="localhost", port = 27017)

client = MongoClient()
db = "vpp_data"
col_vpp = "create_vpp" #database collection
col_site = "create_sites"

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
    Assogned_VPP: str
    Description: str
    
@app.post("/create_vpp")
async def get_created_vpp(request: Request):
#async def get_created_vpp():
    body = await request.json()
    #json.loads take a string as input and returns a dictionary as output.
    #obj = json.loads(body)
    print(body)
    print(type(body)) # type of obj is dict
    with MongoClient() as client:
        msg_col = client[db][col_vpp]
        msg_content = VPP(**body)
        insert_result = msg_col.insert_one(msg_content.dict())
        
        for doc in msg_col.find():
            pp.pprint(doc) # pretty print the returned documents
    return body
    
@app.post("/create_sites")
async def get_created_sites(request: Request):
    body_site = await request.json()
    #json.loads take a string as input and returns a dictionary as output.
    #obj = json.loads(body)
    print(body_site)
    print(type(body_site)) # type of obj is dict
    
    with MongoClient() as client:
        msg_col = client[db][col_site]
        msg_content = Sites(**body_site)
        insert_result = msg_col.insert_one(msg_content.dict())
        
        for doc in msg_col.find():
            pp.pprint(doc) # pretty print the returned documents
    return body_site

@app.get("/get_vpp")
def get_vpp():
    vpp = json.loads(Create_vpp.objects().to_json()) # return all the docs in db collection
    #vpp = Create_vpp.objects()
    pp.pprint(vpp)
    #print(vpp)
    #employees_list = json.loads(employees)
    print(type(vpp)) # print the types of var
    return {"VPP created":  vpp} # retun to the client
    
@app.get("/get_sites")
def get_sites():
    sites = json.loads(Create_sites.objects().to_json()) # return all the docs in db collection
    pp.pprint(sites)
    #print(sites)
    #employees_list = json.loads(employees)
    print(type(sites)) # print the types of var
    return {"Sites created":  sites} # retun to the client     
# @app.get("/get_vpp")
# def get_vpp():
#     vpp_data = json.loads(create_vpp.objects().to_json()) # return all the docs in db collection
#     pp.pprint(vpp_data)
#     print(type(vpp_data)) # print the types of var
#     return {"VPP created":  vpp_data} # retun to the client
    
# @app.get("/get_sites")
# def get_sites():
#     sites_data = json.loads(create_sites.objects().to_json()) # return all the docs in db collection
#     pp.pprint(sites_data)
#     #print(sites)
#     #employees_list = json.loads(employees)
#     print(type(sites_data)) # print the types of var
#     return {"Sites created":  sites_data} # retun to the client 
    
# import asyncio
# loop = asyncio.get_event_loop()
# #await create_vpp.get_created_vpp(Request)
# #prepare_for_get_created_vpp(Request)
# #task = loop.create_task(create_vpp.get_created_vpp(Request))
# #remaining_work_not_depends_on_get_created_vpp(Request)
# try:
#     loop.run_until_complete(get_created_vpp())  
# finally:
#     loop.close()

if __name__ == '__main__':
#     #it will run on port 8000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')
    

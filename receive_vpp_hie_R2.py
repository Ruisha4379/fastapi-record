"""
Update Date: 2022-11-07
Functions included:
1. Created the POST/GET endpoints to receive/return the UI created data for vpp, 
sites and market resources
2. While POST, the received data is saved to mongoDB with the structure of 
-vpp[db]
-- vpp_metadata[col]
-- site_metadata[col]
-- market_resource_metada[col]
3. The GET endpoints for vpp, sites and MR are designed based on the input of the
vpp_name for accessing the vpp and sites data; input of vpp_name and site_name for
accessomg MR data.
4. Add the geocoding endpoint which can return the latitude and longtitude from the
OpenWeather GeoCoding API
5. Add the function to avoid duplicate document in a mongodb collection
"""

from pymongo import MongoClient
from mongoengine import connect
from mongoengine.connection import disconnect
from fastapi import FastAPI, status, Request
from pydantic import BaseModel
from models_hie import Vpp_metadata, Sites_metadata, MarketResource_metadata
from openweathergeo import get_location
from typing import Optional, List, Dict, Union
import uvicorn
import json
import asyncio
#from json import JSONDecodeError
#import requests
#from enum import Enum
import pprint
pp = pprint.PrettyPrinter(indent=4)

app      = FastAPI()
client   = MongoClient()
#db       = "vpp_data"
col_vpp  = "vpp_metadata" # for vpp
col_site = "sites_metadata" # for list of sites
col_mr   = "market_resource_metadata"

class VPP(BaseModel):
    Name: str
    VppID: str
    MarketType: str#['FR', 'DR', 'Reserve', 'Energy']
    ControlArea: str#['CAISO','PJM', 'Singapore PSO', 'Chubu']
    CommunicationProtocol: str#['Open ADR', 'Echonetlite', 'IEC 104']
    FlexUpCost: str
    FlexDownCost: str
    FlexUpCapacity: str # calculated from the site capacity
    FlexDownCapacity: str # calculated from the site capacity
    Description: str
    #Sites: str # Need to be linked with sites mongodb
    
class Sites(BaseModel):  
    Name:str
    SiteID: str
    SiteAddress:str
    AssignedVPP: str
    FlexUpCost: str
    FlexDownCost: str
    FlexUpCapacity: str # calculated from the site capacity
    FlexDownCapacity: str # calculated from the site capacity
    Description: str
    #MarketResource: str
    
class MR(BaseModel):
    Name: str           
    ResourceID: str
    ResourceType: str   
    AssignedVPP: str   
    AssignedSite: str  
    Description: str    
    
@app.post("/create_vpp")
async def get_created_vpp(request: Request): #request: Request
    body = await request.json()
    #json.loads take a string as input and returns a dictionary as output.
    #obj = json.loads(body)
    #Extract the vpp name from the data send by create vpp form UI
    db = body['Name']
    #col_vpp.create_index([('field_i_want_to_index', pymongo.TEXT)], name='search_index', default_language='english')
    #db.col_vpp.createIndex( { user: 1, title: 1, Bank: 1 }, {unique:true} )
    print("VPP name extracted is",db)
    with MongoClient() as client:
        msg_col = client[db][col_vpp]
        msg_content = VPP(**body)
        #print('msg_col type is:', type(msg_col))
        msg_col.create_index([("Name", 1)], unique =True)
        insert_result = msg_col.insert_one(msg_content.dict())
        #Print the lastes inserted collection:
        print('The latest inserted VPP metadata collection is')
        #List the collection in msg_col sorted based on vpp_name
        for doc in msg_col.find().sort('Name',-1).limit(1):
            pp.pprint(doc) # pretty print the returned documents
        
    return body
    
@app.post("/create_sites")
async def get_created_sites(request: Request):
    body_site = await request.json()
# def get_created_sites(request: Request):    
#     body_site = request.json()
    print(body_site)
    #print(type(body_site)) # type of obj is dict
    site_name = body_site['Name']
    site_vpp    = body_site['AssignedVPP']
    print("The VPP assigned for " + site_name + " is:", site_vpp)
    with MongoClient() as client:
        msg_col = client[site_vpp][col_site]
        msg_content = Sites(**body_site)
        msg_col.create_index([("Name", 1)], unique =True)
        insert_result = msg_col.insert_one(msg_content.dict())
        
        for doc in msg_col.find().sort('Name',-1).limit(1):
            pp.pprint(doc)
    return body_site
    
@app.post("/create_market_resource")
async def get_created_mr(request: Request):
    body_mr= await request.json()
    print(body_mr)
    #print(type(body_site)) # type of obj is dict
    mr_name = body_mr['Name']
    mr_vpp  = body_mr['AssignedVPP']
    mr_site = body_mr['AssignedSite']
    print("The VPP assigned for " + mr_name + " is:", mr_vpp)
    print("The site assigned for " + mr_name + " is:", mr_site)
    
    with MongoClient() as client:
        msg_col = client[mr_vpp][col_mr]
        msg_content = MR(**body_mr)
        msg_col.create_index([("Name", 1)], unique =True)
        insert_result = msg_col.insert_one(msg_content.dict())
        
        for doc in msg_col.find().sort('Name',-1).limit(1):
            pp.pprint(doc)
    return body_mr

################################################################################
@app.get("/get_vpp/{vpp_name}") # User input the VPP name to extract the VPP metadata
def get_vpp(vpp_name:str):
    print(vpp_name)
    db_client = connect(db = vpp_name, host="localhost", port = 27017)
    vpp = json.loads(Vpp_metadata.objects().to_json()) # return all the docs in db collection
    #vpp = Create_vpp.objects()
    pp.pprint(vpp)
    print(type(vpp)) # print the types of var
    #close the connection
    #db_client.close()
    return {"VPP created":  vpp} # retun to the client
    
@app.get("/get_sites/{vpp_name}") # User input the VPP name to extract the list of sites
def get_sites(vpp_name:str):
    print(vpp_name)
    sites_client = connect(db = vpp_name, host="localhost", port = 27017)
    sites = json.loads(Sites_metadata.objects().to_json()) # return all the docs in db collection
    pp.pprint(sites)
    print(type(sites)) # print the types of var
    #sites_client.close()
    return {"Sites created":  sites} # retun to the client

#Create the endpoint for UI to inpu the zip_code and country code to extract the lat and lon
@app.get("/get_location/{zip_code}/{country_code}")
def get_loc(zip_code:str,country_code:str):
    loc = get_location(zip_code, country_code)
    print("The site address retrived is: ", loc)
    return {"Site address is: ": loc}

# # User input the vpp_name and the site_name to extract the list of MR under the site and vpp 
@app.get("/get_market_resource/{vpp_name}/{site_name}") 
def get_mr(vpp_name:str, site_name: str): #/{site_name} 
    print(vpp_name)
    print(site_name)
    mr_client = connect(db = vpp_name, host="localhost", port = 27017)
    mrs = json.loads(MarketResource_metadata.objects().to_json()) # return all the docs in db collection
    print("Type of mrs is ", type(mrs))
    # Find and return the documents under the market_resource collection with the called site no.
    mrs_filter = next(
    (item for item in mrs if item['AssignedSite'] == site_name),{})
    #mr_client.close()
    
    return {"Market Resources created for site "  + site_name + "are":  mrs_filter} # retun to the client

if __name__ == '__main__':
#     #it will run on port 8000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')
    

"""
Update Date: 2022-11-07
By: Sai Wei
Simulate the UI post data to the POST endpoint created.
"""
import requests
from fastapi import Request, FastAPI
#from fastapi import APIRouter
import uvicorn
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

url_vpp  = f"http://13.57.5.224:8000/create_vpp"
url_site = f"http://13.57.5.224:8000/create_sites"
url_mr   = f"http://13.57.5.224:8000/create_market_resource"

create_vpp_data = {
    "Name":"VppTest",
    "VppID": "vpp_0035",
    "MarketType": "FR",
    "ControlArea": "CAISO",
    "CommunicationProtocol": "IEC 104",
    "FlexUpCost": "1002.0",
    "FlexDownCost": "0.01",
    "FlexUpCapacity": "100.0",
    "FlexDownCapacity": "1.0",
    "Description": "test"
    #"Sites":"s"
}

create_sites_data1 = {
    "Name":"site_0008",
    "SiteID": "site_0008",
    "SiteAddress":"Lorong Chuan",
    "AssignedVPP": "VppDemo",
    "FlexUpCost": "1002.0",
    "FlexDownCost": "0.01",
    "FlexUpCapacity": "10.0",
    "FlexDownCapacity": "1.0",
    "Description": "str"
    #"MarketResource": "str"
}

create_sites_data2 = {
    "Name":"site_0010",
    "SiteID": "site_0010",
    "SiteAddress":"Bishan",
    "AssignedVPP": "VppDemo",
    "FlexUpCost": "1002.0",
    "FlexDownCost": "0.01",
    "FlexUpCapacity": "10.0",
    "FlexDownCapacity": "1.0",
    "Description": "str"
    #"MarketResource": "str"
}

create_market_resource_data1 = {
    "Name":"microgrid_0002",
    "ResourceID": "microgrid_0002",
    "ResourceType": "microgrid",
    "AssignedVPP": "VppDemo",
    "AssignedSite": "site_0008",
    "Description": "str"
}

create_market_resource_data2 = {
    "Name":"bess_0001",
    "ResourceID": "bess_0001",
    "ResourceType": "bess",
    "AssignedVPP": "VppDemo1",
    "AssignedSite": "site_0002",
    "Description": "str"
}

response_vpp   = requests.post(url_vpp,  json = create_vpp_data) #, json=data
#response_site1 = requests.post(url_site, json = create_sites_data1)
#response_site2 = requests.post(url_site, json = create_sites_data2)
#response_mr1   = requests.post(url_mr,   json = create_market_resource_data1)
#response_mr2   = requests.post(url_mr,   json = create_market_resource_data2)
#print(type(create_vpp_data))
print(response_vpp.text)
print(response_vpp)
#print(response_site1.text)
#print(response_site1)
#print(response_site2.text)
#print(response_site2)
#print(response_mr1.text)
#print(response_mr1)
#print(response_mr2.text)
#print(response_mr2)

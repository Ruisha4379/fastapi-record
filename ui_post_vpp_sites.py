"""
Date: 2022-10-28
Simulate the UI post data to the POST endpoint created.
"""
import requests
from fastapi import Request, FastAPI
#from fastapi import APIRouter
import uvicorn
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

url_vpp = f"http://54.177.121.48:8000/create_vpp"
url_site =f"http://54.177.121.48:8000/create_sites"
create_vpp_data = {
    "Name":"VppDemo",
    "VPP_ID": "vpp_0034",
    "Market_Type": "FR",
    "Control_Area": "CAISO",
    "Communication_Protocol": "IEC 104",
    "Flex_Up_Cost": "1002.0",
    "Flex_Down_Cost": "0.01",
    "Flex_Up_Capacity": "100.0",
    "Flex_Down_Capacity": "1.0",
    "Description": "test",
    "Sites":"s"
}
create_sites_data1 = {
    "Name":"site0001",
    "Site_ID": "site_0001",
    "Site_address":"Lorong Chuan",
    "Assigned_VPP": "VppDemo",
    "Description": "str",
    "Market_resource": "str"
}

create_sites_data2 = {
    "Name":"site_0004",
    "Site_ID": "site_0004",
    "Site_address":"Bishan",
    "Assigned_VPP": "VppDemo",
    "Description": "str",
    "Market_resource": "str"
}

response_vpp = requests.post(url_vpp, json = create_vpp_data) #, json=data
response_site = requests.post(url_site, json = create_sites_data2)
print(type(create_vpp_data))
print(response_vpp.text)
print(response_vpp)
print(response_site.text)
print(response_site)

"""
Simulate the UI post data to the POST endpoint created.
"""
import requests
from fastapi import Request, FastAPI
#from fastapi import APIRouter
import uvicorn
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

BASE = f"http://13.56.255.121:8000/data/vpptree"
create_vpp_data = {
    'Name':'VPP0001',
    'VPP_ID': 'VPP_0001',
    'Market_Type': 'FR',
    'Control_Area': 'CAISO',
    'Communication_Protocol': 'IEC 104',
    'Flex_Up_Cost ($/MWh)': 1000.0,
    'Flex_Down_Cost ($/MWh)': 0.01,
    'Flex_Up_Capacity (MW)': 100.0,
    'Flex_Down_Capacity (MW)': 1.0,
    'Description': 'str',
    'sites':'str'
}
create_sites_data1 = {
    'Name':'site0001',
    'Site_ID': 'site_0001',
    'Site_address':'Lorong Chuan',
    'Assogned_VPP': 'VPP_0001',
    'Description': 'str'
}

create_sites_data2 = {
    'Name':'site0002',
    'Site_ID': 'site_0002',
    'Site_address':'Bishan',
    'Assogned_VPP': 'VPP_0001',
    'Description': 'str'
}
response = requests.post(BASE, json = create_vpp_data) #, json=data

print(response.text)
print(response)

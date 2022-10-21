"""
Get data created from MongoDB database "vpp_data" collection of "create_vpp".
"""
from pymongo import MongoClient
from fastapi import FastAPI, status
from pydantic import BaseModel
from models import Create_vpp # a seperate module to map the data schema in MongoDB, alignment of key, value of data collection 
from mongoengine import connect #connect to mongodb 
from typing import List
import uvicorn
import json
import pprint
pp = pprint.PrettyPrinter(indent=4)

#client = MongoClient()
#db = "vpp_data"
#col = "create_vpp" # database collection

app = FastAPI() 
connect(db = "vpp_data", host="localhost", port = 27017)

@app.get("/query/vpptree")
def get_vpp():
    # map to json is critical, othervise the get method cannot recognize the document
    # defined in the models.py to map the data collection "create_vpp" 
    vpp = json.loads(Create_vpp.objects().to_json()) # return all the employee docs
    #vpp = Create_vpp.objects()
    print(vpp)
    #employees_list = json.loads(employees)
    print(type(vpp)) # print the types of var
    return {"VPP created":  vpp} # retun to the client
    
if __name__ == '__main__':
    #it will run on port 3000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')

"""
GET data from mongDB and return it to client
Source: https://www.youtube.com/watch?v=1h2aQhv8-oI&list=PL4iRawDSyRvWybsXRTommb3acUigWPEsj&index=3&ab_channel=JerinJose 
"""
from fastapi import FastAPI
from models import Employee # seperate module
from mongoengine import connect
import uvicorn
import json

app = FastAPI() 
connect(db = "hrms", host="localhost", port = 27017)

@app.get("/")
def home():
    return {"message": "Hello"}
    
@app.get("/get_all_employees")
def get_all_employees():
    employees = json.loads(Employee.objects().to_json()) # return all the employee docs
    #print(employees)
    #employees_list = json.loads(employees)
    print(type( employees)) # print the types of var
    return {"employees":  employees} # retun to the client
    
if __name__ == '__main__':
    #it will run on port 3000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')

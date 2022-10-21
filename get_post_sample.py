from fastapi import FastAPI, Request, File, UploadFile, Depends
from pydantic import BaseModel
import uvicorn
from enum import Enum # predeine the data type 
from typing import Optional
data = {
    "name": "vpp_xxx",
    "vpp_id": "vpp_0001",
    "status": "OPEN",
    "market_id": "Singapore PSO",
    "market_type":"Energy"
  }
# create the instance of the application
# app is used to provide the path and start the server
app = FastAPI() 
################################################################################
################################################################################
# Create an empty endpoint with url 
@app.get('/data/vpptree')
def get_vpptree(): # provide the variable to the path /ui/333 with int 333
    return {'vpptree': 'VPP tree is to be received'}  
# The url generated is: http://18.144.54.149:8000/data/vpptree
#Using an asynchronous POST method for communication
################################################################################
# Define and empty endpoint that only receives data from post
#Base model
class Item(BaseModel):
    name: str
    description: str
    price: float
    tax: float 
    
@app.post("/items")
async def create_item(item: Item):
    # save the new Item by creating a new instance
    new_item = item(name = item.name, description = item.description,
                    price = item.price, tax = item.tax)
    new_item.save()
    print(item)
    return {'message': "Item added successfully"}
################################################################################
# Post the data to the urs generated at /data/vpptree
@app.post('/send_data')
def post_data(data):
    return 'acknowledge'
################################################################################
# We define the API that gets us on the base url and simply return the 
# data defined above
@app.get("/vpp-tree") # The GET operation we're going to perform with the path "/"
async def index():
    #return {"message": "Hello World. Welcome to the API home page!"}
    return {"message": data}

################################################################################
# Define path parameter
# type the public id + :8000/ui/variable    
@app.get('/data/{tree2}')
def get_vpp_tree(tree2:int): # provide the variable to the path /ui/333 with int 333
    return {'tree2': f'Tree get is {tree2}'}
  
# @app.get('/blog/all')
# def get_all_blogs(): # do not define the var
#     return {'message': 'All blogs provded'}    

# Pass query parameters {page} and {page_size} to the get. All the para can be pre-dertermined
# as default as: get_all_blogs(page = 3, page_size=10)
@app.get('/blog/all')
def get_all_blogs(page, page_size: Optional[int]=None): # page_size is optional para 
    return {'message': f'All {page_size} blogs on page {page}'}
################################################################################
# Combine path and query variables
# Path parameters: {id},{comment_id}
# Query parameters: valid, username
@app.get('/blog/{id}/comments/{comment_id}')
def get_comment(id:int, comment_id:int, valid:bool = True, username:Optional[str]= None): 
    return {'message': f'blog_id {id}, comment_id {comment_id}, valid {valid}, username {username}'}
    
# The complete request is: http://18.144.54.149:8000/blog/45/comments/2?valid=false&username=sw
# The payload of the above request: {"message":"blog_id 45, comment_id 2, valid False, username sw"}
################################################################################
# define the data type:
class BlogType(str, Enum):
    short= 'short'
    story= 'story'
    howto= 'howto'
# define the get operation
@app.get('/blog/type/{type}') # {} means inside is var
def get_blog_type(type:BlogType):
    return {'message':f'Blog type {type}'}

@app.get ('/blog/{id}')
def get_blog(id: int):
    return {'message': f'Blog with id {id}'}

if __name__ == '__main__':
    #it will run on port 3000 and it can receive traffic from anywhere
    uvicorn.run(app,debug=True,port=8000,host='0.0.0.0')

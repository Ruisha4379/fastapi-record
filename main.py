import json
import os
from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
from fastapi.encoders import jsonable_encoder
# pydantic is a parser. It guarantees the types and constraints of the output model, not the input data.
from pydantic import BaseModel
# Mangum is an adapter for running ASGI applications in AWS Lambda to handle Function URL, API Gateway, ALB, and Lambda@Edge events.
from mangum import Mangum


app = FastAPI()
# define a simple get method
@app.get('/')
def index():
  return 'Hellow world!'

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
# define a simple get method
@app.get('/')
def index():
  return 'Hellow world!'

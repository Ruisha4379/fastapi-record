"""
Define the data format in the function Employee
"""
from mongoengine import Document, StringField,IntField, ListField

class Employee(Document):
    name = StringField(max_len=100)
    age = IntField()
    teams= ListField()

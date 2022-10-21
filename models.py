"""
Linkup FASTAPI with MongoDB
"""
from mongoengine import Document, StringField,IntField, ListField
# Need to map to the mongoDB schema for db created "vpp_data"
# The class name should match with the db collection name which is "create_vpp"
class Create_vpp(Document): 
    # name = StringField(max_len=100)
    # age = IntField()
    # teams= ListField()
    name = StringField
    vpp_id = StringField
    status= StringField
    market_id= StringField
    market_type= StringField

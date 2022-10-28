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
    Name = StringField
    VPP_ID = StringField
    Market_Type = StringField
    Control_Area = StringField
    Communication_Protocol = StringField
    Flex_Up_Cost = StringField
    Flex_Down_Cost = StringField
    Flex_Up_Capacity = StringField
    Flex_Down_Capacity = StringField 
    Description = StringField
    Sites = StringField

class Create_sites(Document):
    Name = StringField
    Site_ID = StringField
    Site_address = StringField
    Assogned_VPP = StringField
    Description = StringField
    Market_resource = StringField

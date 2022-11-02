"""
Date: 2022-11-02
Define the data format for the GET endpoint to retrieve data stored at MongoDB
"""
from mongoengine import Document, StringField,IntField, ListField
# Need to map to the mongoDB schema for db created "vpp_data"
# The class name should match with the db collection name which is "create_vpp"

class Vpp_metadata(Document): 
    # name = StringField(max_len=100)
    # age = IntField()
    # teams= ListField()
    Name                  = StringField
    VppID                 = StringField
    MarketType            = StringField
    ControlArea           = StringField
    CommunicationProtocol = StringField
    FlexUpCost            = StringField
    FlexDownCost          = StringField
    FlexUpCapacity        = StringField
    FlexDownCapacity      = StringField 
    Description           = StringField
    #Sites                 = StringField

class Sites_metadata(Document):
    Name           = StringField
    SiteID         = StringField
    SiteAddress    = StringField
    AssignedVPP    = StringField
    Description    = StringField
    #MarketResource = StringField

  
class MarketResource_metadata(Document):
    Name           = StringField
    ResourceID     = StringField
    ResourceType   = StringField
    AssignedVPP   = StringField
    AssignedSite   = StringField
    Description    = StringField
    

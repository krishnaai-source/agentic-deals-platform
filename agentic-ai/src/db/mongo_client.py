# db/mongo_client.py
from pymongo import MongoClient
from ..config import MONGO_URI, MONGO_DB

_client = MongoClient(MONGO_URI)
_db = _client[MONGO_DB]

def skus_collection():
    return _db["skus"]

def inventory_collection():
    return _db["inventory"]

def pricing_collection():
    return _db["pricing"]

def region_config_collection():
    return _db["region_config"]

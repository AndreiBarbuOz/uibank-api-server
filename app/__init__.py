import os
from pymongo import MongoClient

client = MongoClient(os.environ['MONGO_DB_STRING'])
db = client['uibank']
print("init db")

__all__ = ["db"]
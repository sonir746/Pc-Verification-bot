import os
from pymongo import MongoClient


MONGODB_URI = os.getenv('MONGO_URI')
if not MONGODB_URI:
    raise ValueError("Missing MONGO_URI in .env file")

client = MongoClient(MONGODB_URI)
db = client["pc_verification"]
collection = db["users"]

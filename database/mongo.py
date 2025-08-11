import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv('MONGO_URI')
if not MONGODB_URI:
    raise ValueError("Missing MONGO_URI in .env file")

client = MongoClient(MONGODB_URI)
db = client["pc_verification"]
collection = db["users"]

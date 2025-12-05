# src/infrastructure/persistence/client.py
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")

if not MONGO_URI or not DB_NAME:
    raise ValueError(
        "MONGO_URI and DB_NAME must be configured in the .env file."
    )

try:
    mongo_client = MongoClient(MONGO_URI)
    mongo_client.admin.command('ping') 
    print("✅ Successful connection to MongoDB Atlas Core.")
except Exception as e:
    print(f"❌ Error connecting to MongoDB Atlas: {e}")
    # Application should not start without a DB connection in production
    raise e

db = mongo_client[DB_NAME]

# Expose collections
events_collection = db["events"]
teams_collection = db["teams"]
matches_collection = db["matches"]
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb+srv://HK_Digiverse:HK%40Digiverse%40123@cluster0.lcbyqbq.mongodb.net/the_sandras?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = os.getenv("DATABASE_NAME", "the_sandras")

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def connect_to_mongo():
    try:
        # Added timeout to avoid hanging if the connection is bad
        db.client = AsyncIOMotorClient(MONGODB_URL, serverSelectionTimeoutMS=5000)
        # Verify connection
        await db.client.admin.command('ping')
        print(f"DONE: Successfully connected to MongoDB: {MONGODB_URL}")
    except Exception as e:
        print(f"ERROR: Could not connect to MongoDB. Error: {e}")
        # We don't raise here so the app can still start and show health errors

async def close_mongo_connection():
    if db.client:
        db.client.close()
        print("MongoDB connection closed.")

def get_database():
    return db.client[DATABASE_NAME]

from motor.motor_asyncio import AsyncIOMotorClient
import certifi
from app.core.config import settings
from fastapi import HTTPException

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def connect_to_mongo():
    try:
        # Check if URL is valid before attempting connection
        if not settings.MONGODB_URL or "mongodb" not in settings.MONGODB_URL:
            raise ValueError("MONGODB_URL is missing or invalid")

        db.client = AsyncIOMotorClient(
            settings.MONGODB_URL, 
            serverSelectionTimeoutMS=5000,
            tlsCAFile=certifi.where()
        )
        # Verify connection immediately
        await db.client.admin.command('ping')
        print(f"DONE: Successfully connected to MongoDB cluster")
    except Exception as e:
        print(f"ERROR: Could not connect to MongoDB. Error: {e}")
        db.client = None # Explicitly set to None on failure

async def close_mongo_connection():
    if db.client:
        db.client.close()
        print("MongoDB connection closed.")

def get_database():
    if db.client is None:
        print("CRITICAL: Attempted to get database while client is None")
        raise HTTPException(
            status_code=503, 
            detail="Database connection is unavailable. Please check your configuration."
        )
    return db.client[settings.DATABASE_NAME]


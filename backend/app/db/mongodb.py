from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

class Database:
    client: AsyncIOMotorClient = None

db = Database()

async def connect_to_mongo():
    try:
        # Added timeout to avoid hanging if the connection is bad
        db.client = AsyncIOMotorClient(settings.MONGODB_URL, serverSelectionTimeoutMS=5000)
        # Verify connection
        await db.client.admin.command('ping')
        print(f"DONE: Successfully connected to MongoDB: {settings.MONGODB_URL}")
    except Exception as e:
        print(f"ERROR: Could not connect to MongoDB. Error: {e}")
        # We don't raise here so the app can still start and show health errors

async def close_mongo_connection():
    if db.client:
        db.client.close()
        print("MongoDB connection closed.")

def get_database():
    return db.client[settings.DATABASE_NAME]

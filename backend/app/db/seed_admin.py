import asyncio
import os
import sys
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
sys.path.append(os.path.join(os.path.dirname(__file__), "../.."))
from app.core import security

import certifi

# Load env from backend/.env
load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

async def seed_admin():
    print(f"Connecting to MongoDB: {DATABASE_NAME}...")
    try:
        client = AsyncIOMotorClient(
            MONGODB_URL,
            serverSelectionTimeoutMS=5000,
            tlsCAFile=certifi.where()
        )
        # Verify connection
        await client.admin.command('ping')
        db = client[DATABASE_NAME]
        
        admin_user = {
            "username": "Admin",
            "hashed_password": security.get_password_hash("Admin123")
        }
        
        # Check if user exists
        existing_user = await db.users.find_one({"username": admin_user["username"]})
        if existing_user:
            await db.users.update_one(
                {"username": admin_user["username"]},
                {"$set": {"hashed_password": admin_user["hashed_password"]}}
            )
            print(f"SUCCESS: Updated existing admin user: {admin_user['username']}")
        else:
            await db.users.insert_one(admin_user)
            print(f"SUCCESS: Created new admin user: {admin_user['username']}")
        
        client.close()
    except Exception as e:
        print(f"ERROR: Failed to seed admin user. {e}")
        sys.exit(1)

if __name__ == "__main__":
    asyncio.run(seed_admin())

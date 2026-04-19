import asyncio
import os
import sys
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import dns.resolver
import certifi

# Workaround for DNS resolution issues in some environments
try:
    dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
    dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4', '1.1.1.1']
except Exception as e:
    print(f"Warning: Could not configure custom DNS resolver: {e}")

# Load env from backend/.env
# We assume this script is run from the backend directory or via app.py
load_dotenv(os.path.join(os.path.dirname(__file__), "../../.env"))

MONGODB_URL = os.getenv("MONGODB_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")

if not MONGODB_URL:
    print("ERROR: MONGODB_URL not found in environment")
    sys.exit(1)

PROPERTIES = [
    {
        "slug": "cullinan-house",
        "name": "Cullinan House",
        "hero": "/assets/hero-cullinan.jpg",
        "intro": "The central hub of The Sandars later living village, Cullinan House is a Grade II listed building that places you at the centre of the community. Here you'll find the perfect haven for your retirement with open-plan apartments available to buy or rent.",
        "showApartmentNote": "Show apartment available to view",
        "hours": "Open from 10am – 5pm Monday – Friday",
        "featured_image": "/assets/prop-cullinan.jpg",
        "tag": "For Sale",
        "date": "18 November 2024",
        "is_featured": True,
        "apartments": [
            {
                "name": "No.1 Cullinan House", "type": "1 Bedroom", "size": "76 sq m", "price": "On request", "slug": "no-1-cullinan-house",
                "floorplan_image": "/assets/no-1-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.7m x 5.4m", "imperial": "25'3\" x 17'8\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.5m", "imperial": "15'8\" x 11'5\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.2 Cullinan House", "type": "1 Bedroom", "size": "72 sq m", "price": "On request", "slug": "no-2-cullinan-house",
                "floorplan_image": "/assets/no-2-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "6.9m x 5.0m", "imperial": "22'7\" x 16'4\""},
                    {"room": "Bedroom", "metric": "4.3m x 3.5m", "imperial": "14'1\" x 11'5\""},
                    {"room": "Bathroom", "metric": "3.2m x 2.0m", "imperial": "10'5\" x 6'6\""}
                ]
            },
            {
                "name": "No.3 Cullinan House", "type": "1 Bedroom", "size": "72 sq m", "price": "On request", "slug": "no-3-cullinan-house",
                "floorplan_image": "/assets/no-3-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "6.9m x 5.0m", "imperial": "22'7\" x 16'4\""},
                    {"room": "Bedroom", "metric": "4.3m x 3.5m", "imperial": "14'1\" x 11'5\""},
                    {"room": "Bathroom", "metric": "3.2m x 2.0m", "imperial": "10'5\" x 6'6\""}
                ]
            },
            {
                "name": "No.4 Cullinan House", "type": "2 Bedroom", "size": "91 sq m", "price": "On request", "slug": "no-4-cullinan-house",
                "floorplan_image": "/assets/no-4-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.7m x 6.1m", "imperial": "25'3\" x 20'0\""},
                    {"room": "Bedroom 1", "metric": "4.8m x 3.5m", "imperial": "15'8\" x 11'5\""},
                    {"room": "Bedroom 2", "metric": "3.4m x 2.8m", "imperial": "11'1\" x 9'2\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.5 Cullinan House", "type": "1 Bedroom", "size": "74 sq m", "price": "On request", "slug": "no-5-cullinan-house",
                "floorplan_image": "/assets/no-5-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "8.1m x 5.0m", "imperial": "26'6\" x 16'4\""},
                    {"room": "Bedroom", "metric": "4.4m x 3.4m", "imperial": "14'5\" x 11'1\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.6 Cullinan House", "type": "1 Bedroom", "size": "77 sq m", "price": "On request", "slug": "no-6-cullinan-house",
                "floorplan_image": "/assets/no-6-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.7m x 5.4m", "imperial": "25'3\" x 17'8\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.5m", "imperial": "15'8\" x 11'5\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.7 Cullinan House", "type": "2 Bedroom", "size": "101 sq m", "price": "On request", "slug": "no-7-cullinan-house",
                "floorplan_image": "/assets/no-7-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.9m x 6.9m", "imperial": "25'11\" x 22'7\""},
                    {"room": "Bedroom 1", "metric": "5.3m x 3.3m", "imperial": "17'4\" x 10'9\""},
                    {"room": "Bedroom 2", "metric": "4.3m x 3.1m", "imperial": "14'1\" x 10'2\""},
                    {"room": "Bathroom", "metric": "3.2m x 2.2m", "imperial": "10'5\" x 7'2\""}
                ]
            },
            {
                "name": "No.11 Cullinan House", "type": "1 Bedroom", "size": "66 sq m", "price": "On request", "slug": "no-11-cullinan-house",
                "floorplan_image": "/assets/no-11-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "6.8m x 5.5m", "imperial": "22'3\" x 18'0\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.4m", "imperial": "15'8\" x 11'1\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.13 Cullinan House", "type": "1 Bedroom", "size": "61 sq m", "price": "On request", "slug": "no-13-cullinan-house",
                "floorplan_image": "/assets/no-13-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "6.8m x 4.2m", "imperial": "22'3\" x 13'9\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.2m", "imperial": "15'8\" x 10'5\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.14 Cullinan House", "type": "1 Bedroom", "size": "61 sq m", "price": "On request", "slug": "no-14-cullinan-house",
                "floorplan_image": "/assets/no-14-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "6.8m x 4.2m", "imperial": "22'3\" x 13'9\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.2m", "imperial": "15'8\" x 10'5\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.15 Cullinan House", "type": "2 Bedroom", "size": "83 sq m", "price": "On request", "slug": "no-15-cullinan-house",
                "floorplan_image": "/assets/no-15-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.7m x 5.5m", "imperial": "25'3\" x 18'0\""},
                    {"room": "Bedroom 1", "metric": "4.8m x 3.4m", "imperial": "15'8\" x 11'1\""},
                    {"room": "Bedroom 2", "metric": "3.5m x 2.8m", "imperial": "11'5\" x 9'2\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.16 Cullinan House", "type": "1 Bedroom", "size": "61 sq m", "price": "On request", "slug": "no-16-cullinan-house",
                "floorplan_image": "/assets/no-16-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "6.8m x 4.2m", "imperial": "22'3\" x 13'9\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.2m", "imperial": "15'8\" x 10'5\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.18 Cullinan House", "type": "1 Bedroom", "size": "77 sq m", "price": "On request", "slug": "no-18-cullinan-house",
                "floorplan_image": "/assets/no-18-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.7m x 5.4m", "imperial": "25'3\" x 17'8\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.5m", "imperial": "15'8\" x 11'5\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.19 Cullinan House", "type": "1 Bedroom", "size": "67 sq m", "price": "On request", "slug": "no-19-cullinan-house",
                "floorplan_image": "/assets/no-19-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "6.8m x 4.5m", "imperial": "22'3\" x 14'9\""},
                    {"room": "Bedroom", "metric": "4.8m x 3.4m", "imperial": "15'8\" x 11'1\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.21 Cullinan House", "type": "1 Bedroom", "size": "74 sq m", "price": "On request", "slug": "no-21-cullinan-house",
                "floorplan_image": "/assets/no-21-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "8.1m x 5.0m", "imperial": "26'6\" x 16'4\""},
                    {"room": "Bedroom", "metric": "4.4m x 3.4m", "imperial": "14'5\" x 11'1\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.1m", "imperial": "9'2\" x 6'10\""}
                ]
            },
            {
                "name": "No.22 Cullinan House", "type": "2 Bedroom", "size": "102 sq m", "price": "On request", "slug": "no-22-cullinan-house",
                "floorplan_image": "/assets/no-22-cullinan-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.9m x 6.9m", "imperial": "25'11\" x 22'7\""},
                    {"room": "Bedroom 1", "metric": "5.3m x 3.3m", "imperial": "17'4\" x 10'9\""},
                    {"room": "Bedroom 2", "metric": "4.3m x 3.1m", "imperial": "14'1\" x 10'2\""},
                    {"room": "Bathroom", "metric": "3.2m x 2.2m", "imperial": "10'5\" x 7'2\""}
                ]
            },
        ]
    },
    {
        "slug": "pollards-court",
        "name": "Pollards Court",
        "hero": "/assets/hero-pollards.jpg",
        "intro": "Exuding contemporary elegance, Pollards Court offers a collection of luxury apartments designed for modern retirement living. Each home is finished to an exceptional standard with high-quality specifications throughout.",
        "showApartmentNote": "Show apartment available to view",
        "hours": "Open from 10am – 5pm Monday – Friday",
        "featured_image": "/assets/prop-pollards.jpg",
        "tag": "For Sale",
        "date": "22 November 2024",
        "is_featured": True,
        "apartments": [
            {
                "name": "No.1 Pollards Court", "type": "2 Bedroom", "size": "124 sq m", "price": "On request", "slug": "no-1-pollards-court",
                "floorplan_image": "/assets/no-1-pollards-court-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "8.9m x 5.0m", "imperial": "29'2\" x 16'4\""},
                    {"room": "Bedroom 1", "metric": "5.7m x 4.7m", "imperial": "18'8\" x 15'5\""},
                    {"room": "Bedroom 2", "metric": "4.5m x 3.8m", "imperial": "14'9\" x 12'5\""},
                    {"room": "Bathroom", "metric": "3.0m x 2.0m", "imperial": "9'10\" x 6'6\""},
                    {"room": "Utility", "metric": "2.3m x 1.5m", "imperial": "7'6\" x 4'11\""}
                ]
            },
            {
                "name": "No.4 Pollards Court", "type": "2 Bedroom", "size": "124 sq m", "price": "On request", "slug": "no-4-pollards-court",
                "floorplan_image": "/assets/no-4-pollards-court-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "8.9m x 5.0m", "imperial": "29'2\" x 16'4\""},
                    {"room": "Bedroom 1", "metric": "5.7m x 4.7m", "imperial": "18'8\" x 15'5\""},
                    {"room": "Bedroom 2", "metric": "4.5m x 3.8m", "imperial": "14'9\" x 12'5\""},
                    {"room": "Bathroom", "metric": "3.0m x 2.0m", "imperial": "9'10\" x 6'6\""},
                    {"room": "Utility", "metric": "2.3m x 1.5m", "imperial": "7'6\" x 4'11\""}
                ]
            },
        ]
    },
    {
        "slug": "eastley-end-house",
        "name": "Eastley End House",
        "hero": "/assets/hero-eastley.jpg",
        "intro": "Exuding Georgian charm and character, Eastley End House is a three-storey block originally built in the late 18th century and contains a number of luxury apartments. A grade II listed building, Eastley End House is the perfect place to combine all your modern comforts with some historic charm.",
        "showApartmentNote": "Show apartment available to view",
        "hours": "Open from 10am – 5pm Monday – Friday",
        "featured_image": "/assets/prop-eastley.jpg",
        "tag": "For Sale",
        "date": "22 November 2024",
        "is_featured": True,
        "apartments": [
            {
                "name": "No.4 Eastley End House", "type": "2 Bedroom", "size": "118 sq m", "price": "On request", "slug": "no-4-eastley-end-house",
                "floorplan_image": "/assets/no-4-eastley-end-house-fp.svg",
                "dimensions": [
                    {"room": "Living / Kitchen / Dining", "metric": "7.2m x 5.8m", "imperial": "23'7\" x 19'0\""},
                    {"room": "Bedroom 1", "metric": "4.2m x 3.8m", "imperial": "13'9\" x 12'5\""},
                    {"room": "Bedroom 2", "metric": "3.8m x 3.1m", "imperial": "12'5\" x 10'2\""},
                    {"room": "Bathroom", "metric": "2.8m x 2.0m", "imperial": "9'2\" x 6'6\""}
                ]
            },
            {"name": "No.6 Eastley End House", "type": "1 Bedroom", "size": "92 sq m", "price": "On request", "slug": "no-6-eastley-end-house"},
        ]
    },
    {
        "slug": "meadlake-house",
        "name": "Meadlake House",
        "hero": "/assets/hero-meadlake.jpg",
        "intro": "A grade 2 listed Georgian House offering one and two bedroom luxury living apartments, including Duplex and Penthouse options.Set in stunning picturesque gardens and parkland, it benefits from a whole range of amenities right on its doorstep.",
        "showApartmentNote": "Show apartment available to view",
        "hours": "Open from 10am – 5pm Monday – Friday",
        "featured_image": "/assets/prop-meadlake.jpg",
        "is_featured": False,
        "apartments": [
            {
                "name": "No.2 Meadlake House", "type": "1 Bedroom", "size": "88 sq m", "price": "On request", "slug": "no-2-meadlake-house",
                "floorplan_image": "/assets/no-2-meadlake-house-fp.svg"
            },
            {"name": "No.5 Meadlake House", "type": "2 Bedroom Duplex", "size": "156 sq m", "price": "On request", "slug": "no-5-meadlake-house"},
            {"name": "Penthouse, Meadlake House", "type": "2 Bedroom Penthouse", "size": "182 sq m", "price": "On request", "slug": "penthouse-meadlake-house"},
        ]
    }
]

async def seed():
    print(f"Connecting to {DATABASE_NAME}...")
    try:
        client = AsyncIOMotorClient(
            MONGODB_URL,
            serverSelectionTimeoutMS=5000,
            tlsCAFile=certifi.where()
        )
        # Verify connection
        await client.admin.command('ping')
        print("Connected successfully!")
    except Exception as e:
        print(f"ERROR: Could not connect to MongoDB Atlas. Error: {e}")
        print("Tip: Ensure your IP is whitelisted in MongoDB Atlas and your internet is working.")
        return

    db = client[DATABASE_NAME]
    
    # Clear existing properties
    await db.properties.delete_many({})
    print("Cleared existing properties.")
    
    # Insert new properties
    result = await db.properties.insert_many(PROPERTIES)
    print(f"Successfully seeded {len(result.inserted_ids)} properties.")
    
    client.close()

if __name__ == "__main__":
    asyncio.run(seed())

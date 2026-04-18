from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from mongodb import connect_to_mongo, close_mongo_connection, get_database
from property_model import PropertyModel, PropertyResponse
from inquiry_model import InquiryModel, InquiryResponse
from typing import List

app = FastAPI(title="The Sandras API")

# Enable CORS for the frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {"message": "Welcome to The Sandras API with MongoDB"}

@app.get("/api/properties", response_model=List[PropertyResponse])
async def get_properties():
    db = get_database()
    properties = []
    async for prop in db.properties.find():
        # Convert _id to string for the response
        prop["_id"] = str(prop["_id"])
        properties.append(prop)
    return properties

@app.get("/api/properties/{slug}", response_model=PropertyResponse)
async def get_property(slug: str):
    db = get_database()
    prop = await db.properties.find_one({"slug": slug})
    if prop:
        prop["_id"] = str(prop["_id"])
        return prop
    raise HTTPException(status_code=404, detail="Property not found")

@app.post("/api/properties", response_model=PropertyResponse)
async def create_property(property: PropertyModel):
    db = get_database()
    new_prop = await db.properties.insert_one(property.dict())
    created_prop = await db.properties.find_one({"_id": new_prop.inserted_id})
    created_prop["_id"] = str(created_prop["_id"])
    return created_prop

@app.post("/api/inquiries", response_model=InquiryResponse)
async def create_inquiry(inquiry: InquiryModel):
    db = get_database()
    new_inquiry = await db.inquiries.insert_one(inquiry.dict())
    created_inquiry = await db.inquiries.find_one({"_id": new_inquiry.inserted_id})
    created_inquiry["_id"] = str(created_inquiry["_id"])
    return created_inquiry

@app.get("/api/inquiries", response_model=List[InquiryResponse])
async def get_inquiries():
    db = get_database()
    inquiries = []
    async for inquiry in db.inquiries.find().sort("createdAt", -1):
        inquiry["_id"] = str(inquiry["_id"])
        inquiries.append(inquiry)
    return inquiries

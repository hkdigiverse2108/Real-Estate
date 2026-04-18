from fastapi import APIRouter, HTTPException
from typing import List
from app.db.mongodb import get_database
from app.models.property import PropertyModel, PropertyResponse

router = APIRouter()

@router.get("/", response_model=List[PropertyResponse])
async def get_properties():
    db = get_database()
    properties = []
    async for prop in db.properties.find():
        prop["_id"] = str(prop["_id"])
        properties.append(prop)
    return properties

@router.get("/{slug}", response_model=PropertyResponse)
async def get_property(slug: str):
    db = get_database()
    prop = await db.properties.find_one({"slug": slug})
    if prop:
        prop["_id"] = str(prop["_id"])
        return prop
    raise HTTPException(status_code=404, detail="Property not found")

@router.post("/", response_model=PropertyResponse)
async def create_property(property: PropertyModel):
    db = get_database()
    new_prop = await db.properties.insert_one(property.dict())
    created_prop = await db.properties.find_one({"_id": new_prop.inserted_id})
    created_prop["_id"] = str(created_prop["_id"])
    return created_prop

from fastapi import APIRouter
from typing import List
from app.db.mongodb import get_database
from app.models.inquiry import InquiryModel, InquiryResponse

router = APIRouter()

@router.post("/", response_model=InquiryResponse)
async def create_inquiry(inquiry: InquiryModel):
    db = get_database()
    new_inquiry = await db.inquiries.insert_one(inquiry.dict())
    created_inquiry = await db.inquiries.find_one({"_id": new_inquiry.inserted_id})
    created_inquiry["_id"] = str(created_inquiry["_id"])
    return created_inquiry

@router.get("/", response_model=List[InquiryResponse])
async def get_inquiries():
    db = get_database()
    inquiries = []
    async for inquiry in db.inquiries.find().sort("createdAt", -1):
        inquiry["_id"] = str(inquiry["_id"])
        inquiries.append(inquiry)
    return inquiries

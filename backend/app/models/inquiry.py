from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class InquiryModel(BaseModel):
    title: Optional[str] = None
    firstName: Optional[str] = None
    surname: Optional[str] = None
    email: EmailStr
    telephone: Optional[str] = None
    postcode: Optional[str] = None
    message: Optional[str] = None
    property: Optional[str] = None
    apartment: Optional[str] = None
    createdAt: datetime = Field(default_factory=datetime.utcnow)

class InquiryResponse(InquiryModel):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True

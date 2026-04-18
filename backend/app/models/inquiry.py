from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class InquiryModel(BaseModel):
    title: Optional[str] = None
    firstName: str
    surname: str
    email: EmailStr
    telephone: Optional[str] = None
    postcode: Optional[str] = None
    createdAt: datetime = Field(default_factory=datetime.utcnow)

class InquiryResponse(InquiryModel):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True

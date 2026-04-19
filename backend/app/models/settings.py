from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class SiteSettingsModel(BaseModel):
    phone: str = Field(..., description="Main contact phone number")
    email: EmailStr = Field(..., description="Main contact email address")
    address: str = Field(..., description="Full physical address")
    instagram: Optional[str] = None
    facebook: Optional[str] = None
    linkedin: Optional[str] = None

class SiteSettingsResponse(SiteSettingsModel):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True

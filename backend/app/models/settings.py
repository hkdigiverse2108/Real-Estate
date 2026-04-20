from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class SiteSettingsModel(BaseModel):
    phone: Optional[str] = Field(None, description="Main contact phone number")
    email: Optional[str] = Field(None, description="Main contact email address")
    address: Optional[str] = Field(None, description="Full physical address")
    instagram: Optional[str] = None
    facebook: Optional[str] = None
    linkedin: Optional[str] = None
    video_url: Optional[str] = None

class SiteSettingsResponse(SiteSettingsModel):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True

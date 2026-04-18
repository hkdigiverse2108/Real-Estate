from pydantic import BaseModel, Field
from typing import List, Optional

class Apartment(BaseModel):
    name: str
    type: str
    size: str
    price: str
    slug: str

class PropertyModel(BaseModel):
    slug: str
    name: str
    hero: str
    intro: str
    showApartmentNote: str
    hours: str
    apartments: List[Apartment]

class PropertyResponse(PropertyModel):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True

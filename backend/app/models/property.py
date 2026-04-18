from pydantic import BaseModel, Field
from typing import List, Optional

class Dimension(BaseModel):
    room: str
    metric: str
    imperial: str

class Apartment(BaseModel):
    name: str
    type: str
    size: str
    price: str
    slug: str
    hero_image: Optional[str] = None
    floorplan_image: Optional[str] = None
    location_map_image: Optional[str] = None
    dimensions: List[Dimension] = []

class PropertyModel(BaseModel):
    slug: str
    name: str
    hero: str
    intro: str
    showApartmentNote: str
    hours: str
    apartments: List[Apartment]
    # Fields for featured list (Availability section)
    tag: Optional[str] = "For Sale"
    date: Optional[str] = None
    featured_image: Optional[str] = None
    is_featured: bool = False

class PropertyResponse(PropertyModel):
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True
        json_schema_extra = {
            "example": {
                "slug": "luxury-villa",
                "name": "Luxury Villa",
                "hero": "/images/hero.jpg",
                "intro": "A beautiful villa.",
                "showApartmentNote": "Note",
                "hours": "9-5",
                "apartments": []
            }
        }

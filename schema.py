from pydantic import BaseModel


class PlaceSchema(BaseModel):
    title: str
    description: str
    latitude: float
    longitude: float
    img_url: str
    date_start: str
    date_end: str
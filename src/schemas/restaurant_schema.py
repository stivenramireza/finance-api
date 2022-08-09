from pydantic import BaseModel


class RestaurantSchema(BaseModel):
    name: str
    latitude: float
    longitude: float

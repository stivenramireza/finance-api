from pydantic import BaseModel


class RestaurantSchema(BaseModel):
    name: str = None
    latitude: float = None
    longitude: float = None
    city: str = None

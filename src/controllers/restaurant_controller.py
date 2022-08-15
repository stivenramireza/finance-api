from typing import Optional

from fastapi import APIRouter, Depends, Query, status

from src.schemas.restaurant_schema import RestaurantSchema
from src.services import restaurant_service
from src.middlewares.jwt_middleware import JWTBearer


router = APIRouter(prefix='/restaurants', tags=['Restaurants'])


@router.get(
    path='',
    status_code=status.HTTP_200_OK,
    summary='Near restaurants',
)
def get_restaurants(
    city: Optional[str] = Query(default=None, example='Medellín'),
    latitude: Optional[float] = Query(default=None, example=6.1514783),
    longitude: Optional[float] = Query(default=None, example=-75.6176184),
    jwt_auth: JWTBearer = Depends(JWTBearer()),
) -> list[RestaurantSchema]:
    return restaurant_service.get_restaurants(city, latitude, longitude)

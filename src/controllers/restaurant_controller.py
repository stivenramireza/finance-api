from typing import Optional

from fastapi import APIRouter, Depends, Query, status

from src.schemas.restaurant_schema import RestaurantSchema
from src.services import restaurant_service
from src.middlewares.jwt_middleware import JWTBearer


router = APIRouter(prefix='/restaurants', tags=['restaurant-service'])


@router.get(
    path='',
    status_code=status.HTTP_200_OK,
    summary='Get near restaurants',
)
def get_restaurants(
    latitude: float = Query(example=6.1514783),
    longitude: float = Query(example=-75.6176184),
    radius: Optional[float] = Query(gt=1, le=5, default=3, example=3),
    jwt_auth: JWTBearer = Depends(JWTBearer()),
) -> list[RestaurantSchema]:
    return restaurant_service.get_restaurants(latitude, longitude, radius)

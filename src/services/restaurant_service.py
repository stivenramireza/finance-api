from fastapi import HTTPException, status

from src.schemas.restaurant_schema import RestaurantSchema
from src.repositories import restaurant_repository
from src.services import location_service
from src.utils.mapper import map_restaurants


def get_restaurants(
    city: str, latitude: float, longitude: float
) -> list[RestaurantSchema]:
    restaurants = restaurant_repository.get_restaurants()
    restaurants = map_restaurants(restaurants)

    if city:
        restaurants = get_restaurants_by_city(restaurants, city)
    else:
        restaurants = get_restaurants_by_latitude_and_longitude(
            restaurants, latitude, longitude
        )

    if not restaurants:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Restaurants not found',
        )

    restaurants = list(
        map(
            lambda r: RestaurantSchema(
                name=r.get('name'),
                latitude=r.get('latitude'),
                longitude=r.get('longitude'),
                city=r.get('city'),
            ),
            restaurants,
        )
    )

    return restaurants


def get_restaurants_by_latitude_and_longitude(
    restaurants: list[dict[str, any]], latitude: float, longitude: float
) -> list[dict[str, any]]:
    return list(
        location_service.get_near_locations(restaurants, latitude, longitude)
    )


def get_restaurants_by_city(
    restaurants: list[dict[str, any]], city: str
) -> list[dict[str, any]]:
    return list(
        filter(lambda r: city.lower() in r.get('city').lower(), restaurants)
    )

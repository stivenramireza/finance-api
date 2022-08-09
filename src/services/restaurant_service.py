from src.schemas.restaurant_schema import RestaurantSchema


def get_restaurants(
    latitude: float, longitude: float, radius: float
) -> list[RestaurantSchema]:
    restaurants = [
        RestaurantSchema(
            name=f'Restaurant {i + 1}', latitude=latitude, longitude=longitude
        )
        for i in range(4)
    ]
    return restaurants

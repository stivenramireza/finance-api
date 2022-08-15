def map_restaurants(restaurants: list[dict[str, any]]) -> list[dict[str, any]]:
    restaurants = list(
        filter(
            lambda r: r.get('name'),
            restaurants,
        )
    )

    restaurants = list(
        map(
            lambda r: {
                'name': r.get('name'),
                'latitude': r.get('latitude'),
                'longitude': r.get('longitude'),
                'distance': r.get('distance'),
                'city': r.get('location_string').split(',')[0],
            },
            restaurants,
        )
    )

    return restaurants

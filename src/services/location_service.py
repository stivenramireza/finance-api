from typing import Generator

from haversine import haversine, Unit

RADIUS = 10  # Km


def get_near_locations(
    locations: list[dict[str, any]], latitude: float, longitude: float
) -> Generator:
    for index, value in enumerate(locations):
        source = latitude, longitude
        destination = (
            float(locations[index]['latitude']),
            float(locations[index]['longitude']),
        )

        distance = haversine(source, destination, unit=Unit.KILOMETERS)
        if distance <= RADIUS:
            yield value

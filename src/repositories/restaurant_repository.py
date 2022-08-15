import requests
from requests.exceptions import HTTPError

from src.utils.secrets import secrets
from src.utils.logger import logger


DEFAULT_LATITUDE = 6.1514783
DEFAULT_LONGITUDE = -75.6176184
DEFAULT_RADIUS = 10  # Km
travel_advisor_secrets = secrets.get('TRAVEL_ADVISOR')


def get_restaurants() -> list[dict[str, any]]:
    try:
        response = requests.get(
            '{url}/restaurants/list-by-latlng'.format(
                url=travel_advisor_secrets.get('api_url')
            ),
            headers={
                'X-RapidAPI-Key': travel_advisor_secrets.get('api_key'),
                'X-RapidAPI-Host': travel_advisor_secrets.get('host'),
            },
            params={
                'latitude': DEFAULT_LATITUDE,
                'longitude': DEFAULT_LONGITUDE,
                'distance': DEFAULT_RADIUS,
            },
        )
        response.raise_for_status()
        return response.json().get('data')
    except HTTPError as e:
        logger.error(f'Error to get restaurants from Travel Advisor API: {e}')
        return []

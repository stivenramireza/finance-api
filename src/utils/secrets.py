import os

secrets = {
    'APP': {
        'url': os.getenv('URL'),
    },
    'POSTGRES': {
        'host': os.getenv('POSTGRES_HOST'),
        'port': os.getenv('POSTGRES_PORT'),
        'schema': os.getenv('POSTGRES_SCHEMA'),
        'user': os.getenv('POSTGRES_USER'),
        'password': os.getenv('POSTGRES_PASSWORD'),
    },
    'REDIS': {
        'host': os.getenv('REDIS_HOST'),
        'port': os.getenv('REDIS_PORT'),
        'password': os.getenv('REDIS_PASSWORD'),
    },
    'JWT': {
        'private_key': os.getenv('JWT_PRIVATE_KEY'),
        'public_key': os.getenv('JWT_PUBLIC_KEY'),
    },
    'TRAVEL_ADVISOR': {
        'api_url': os.getenv('TRAVEL_ADVISOR_API_URL'),
        'api_key': os.getenv('TRAVEL_ADVISOR_API_KEY'),
        'host': os.getenv('TRAVEL_ADVISOR_HOST'),
    },
}

import os

from dotenv import load_dotenv

from src.utils.logger import logger


ENV = os.getenv('ENV')
if ENV == 'production':
    dotenv_path = '.env'
    logger.info('Using production environment variables')
else:
    dotenv_path = '.env.dev'
    logger.info('Using development environment variables')

exists_secrets_file = os.path.exists(dotenv_path)

if not exists_secrets_file:
    raise Exception('env file doesn\'t exist')

load_dotenv(dotenv_path)


secrets = {
    'APP': {
        'port': os.getenv('PORT'),
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
}

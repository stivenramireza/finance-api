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
    'DB': {
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT'),
        'schema': os.getenv('DB_SCHEMA'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
    },
    'JWT': {
        'private_key': os.getenv('JWT_PRIVATE_KEY'),
        'public_key': os.getenv('JWT_PUBLIC_KEY'),
    },
}

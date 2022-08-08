from redis import Redis
from redis.exceptions import ConnectionError

from src.utils.secrets import secrets
from src.utils.logger import logger

redis_secrets = secrets.get('REDIS')


try:
    redis_client = Redis(
        host=redis_secrets.get('host'),
        port=redis_secrets.get('port'),
        password=redis_secrets.get('password'),
    )
except ConnectionError as e:
    logger.error(f'Error to connect to Redis database: {e}')

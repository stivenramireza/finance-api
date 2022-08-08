from redis import Redis, ConnectionPool
from redis.exceptions import ConnectionError

from src.utils.secrets import secrets
from src.utils.logger import logger

redis_secrets = secrets.get('REDIS')

try:
    redis_pool = ConnectionPool(
        host=redis_secrets.get('host'),
        port=redis_secrets.get('port'),
        password=redis_secrets.get('password'),
    )
    redis_conn = Redis(connection_pool=redis_pool)
except ConnectionError:
    logger.error('Error to connect to Redis database')

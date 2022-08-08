import json
from redis import Redis

TOKEN_BLACKLIST = 'tokens'


def save_token(redis_conn: Redis, token: str) -> bool:
    blacklist = redis_conn.get(TOKEN_BLACKLIST)
    if not blacklist:
        blacklist = []
        redis_conn.set(TOKEN_BLACKLIST, json.dumps(blacklist))

    if token not in blacklist:
        blacklist.append(token)
        redis_conn.set(TOKEN_BLACKLIST, blacklist)

    return True

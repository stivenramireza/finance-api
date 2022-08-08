from redis import Redis

TOKEN_BLACKLIST = 'tokens'


def get_tokens(client: Redis) -> list[str]:
    blacklist_length = client.llen(TOKEN_BLACKLIST)
    binary_tokens = client.lrange(TOKEN_BLACKLIST, 0, blacklist_length)
    tokens = list(map(lambda t: t.decode('utf-8'), binary_tokens))
    if not tokens:
        return []

    return tokens


def save_token(client: Redis, token: str) -> bool:
    client.rpush(TOKEN_BLACKLIST, token)
    return True

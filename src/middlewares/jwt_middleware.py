from uuid import uuid4
from datetime import datetime, timedelta

import jwt

from src.utils.secrets import secrets


ENCRYPTION_ALGORITHM = 'RS256'
TOKEN_USE = 'access'
JWT_EXPIRATION_TIME = 30  # Minutes

app_secrets = secrets.get('APP')
jwt_secrets = secrets.get('JWT')


def get_jwt_claims(user_identifier: str) -> dict[str, any]:
    current_date = datetime.utcnow()
    expiration_date = current_date + timedelta(minutes=JWT_EXPIRATION_TIME)

    current_time = int(current_date.timestamp())
    expiration_time = int(expiration_date.timestamp())

    token_identifier = str(uuid4())

    return {
        'sub': user_identifier,
        'aud': app_secrets.get('url'),
        'token_use': TOKEN_USE,
        'auth_time': current_time,
        'iss': app_secrets.get('url'),
        'exp': expiration_time,
        'iat': current_time,
        'jti': token_identifier,
    }


def generate_access_token(user_identifier: str) -> str:
    payload = get_jwt_claims(user_identifier)
    private_key = jwt_secrets.get('private_key').encode('utf-8')

    return jwt.encode(
        payload=payload, key=private_key, algorithm=ENCRYPTION_ALGORITHM
    )


def get_payload(token: str) -> dict[str, any]:
    return jwt.decode(
        jwt=token,
        key=jwt_secrets.get('public_key').encode('utf-8'),
        audience=app_secrets.get('url'),
        algorithms=[ENCRYPTION_ALGORITHM],
    )

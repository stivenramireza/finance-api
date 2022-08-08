from uuid import uuid4
from typing import Optional
from datetime import datetime, timedelta

from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt

from src.utils.secrets import secrets

BEARER_AUTH = 'Bearer'
ENCRYPTION_ALGORITHM = 'RS256'
TOKEN_USE = 'access'
JWT_EXPIRATION_TIME = 30  # Minutes

app_secrets = secrets.get('APP')
jwt_secrets = secrets.get('JWT')


class JWTBearer(HTTPBearer):
    def __init__(self, auto_error: bool = True) -> None:
        super(JWTBearer, self).__init__(auto_error=auto_error)

    async def __call__(
        self, request: Request
    ) -> Optional[HTTPAuthorizationCredentials]:
        credentials = await super(JWTBearer, self).__call__(request)
        if not credentials:
            raise HTTPException(status_code=401, detail='Missing credentials')

        if not credentials.scheme == BEARER_AUTH:
            raise HTTPException(
                status_code=401, detail='Invalid authentication scheme'
            )

        payload = self.get_payload(credentials.credentials)
        if not payload:
            raise HTTPException(
                status_code=401, detail='Invalid or expired token'
            )

        return {'sub': payload.get('sub'), 'token': credentials.credentials}

    @staticmethod
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

    @staticmethod
    def generate_access_token(payload: dict[str, any]) -> str:
        private_key = jwt_secrets.get('private_key').encode('utf-8')

        return jwt.encode(
            payload=payload,
            key=private_key,
            algorithm=ENCRYPTION_ALGORITHM,
        )

    def get_payload(self, token: str) -> dict[str, any]:
        try:
            return jwt.decode(
                jwt=token,
                key=jwt_secrets.get('public_key').encode('utf-8'),
                audience=app_secrets.get('url'),
                algorithms=[ENCRYPTION_ALGORITHM],
            )
        except Exception:
            return None

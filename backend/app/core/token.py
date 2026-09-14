from datetime import datetime, timedelta, timezone
from typing import Literal

import jwt

from app.core.config import get_settings

settings = get_settings()

TokenType = Literal["access", "refresh"]


def create_token(
    subject: str,
    token_type: TokenType,
    expires_delta: timedelta,
) -> str:
    now = datetime.now(timezone.utc)

    payload = {
        "sub": subject,
        "type": token_type,
        "iat": now,
        "exp": now + expires_delta,
    }

    return jwt.encode(
        payload,
        settings.jwt_secret_key,
        algorithm=settings.jwt_algorithm,
    )


def create_access_token(subject: str) -> str:
    return create_token(
        subject=subject,
        token_type="access",
        expires_delta=timedelta(
            minutes=settings.access_token_expire_minutes,
        ),
    )


def create_refresh_token(subject: str) -> str:
    return create_token(
        subject=subject,
        token_type="refresh",
        expires_delta=timedelta(
            days=settings.refresh_token_expire_days,
        ),
    )


def decode_token(token: str) -> dict:
    return jwt.decode(
        token,
        settings.jwt_secret_key,
        algorithms=[settings.jwt_algorithm],
    )
from uuid import UUID

from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.security import hash_password, verify_password
from app.core.token import create_access_token, create_refresh_token
from app.repositories.user import UserRepository
from app.schemas.auth import TokenResponse, UserCreate, UserResponse


class AuthService:
    def __init__(self, session: AsyncSession) -> None:
        self.repository = UserRepository(session)

    async def register(self, user_data: UserCreate) -> UserResponse:
        existing_user = await self.repository.get_by_email(
            user_data.email
        )

        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="A user with this email already exists.",
            )

        user = await self.repository.create(
            email=user_data.email,
            password_hash=hash_password(user_data.password),
        )

        return UserResponse(
            id=str(user.id),
            email=user.email,
        )

    async def login(
        self,
        email: str,
        password: str,
    ) -> TokenResponse:
        user = await self.repository.get_by_email(email)

        if user is None or not verify_password(
            password,
            user.password_hash,
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password.",
                headers={"WWW-Authenticate": "Bearer"},
            )

        return TokenResponse(
            access_token=create_access_token(str(user.id)),
            refresh_token=create_refresh_token(str(user.id)),
        )

    async def get_user(self, user_id: UUID) -> UserResponse:
        user = await self.repository.get_by_id(user_id)

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found.",
            )

        return UserResponse(
            id=str(user.id),
            email=user.email,
        )
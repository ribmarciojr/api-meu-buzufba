from decorators.create_session import create_session
from sqlmodel import Session, select
from models.user import User
from fastapi import HTTPException, Response
from config.jwt import create_access_token
from enums.roles import UserRoleEnum

class SignInService:

    @staticmethod
    @create_session
    def signin(session: Session, email: str, password: str, response: Response) -> dict:
        query = select(User).where(User.email == email)
        user = session.exec(query).first()

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        if user.password != password:
            raise HTTPException(status_code=401, detail="Invalid password")

        token_data = {
            "email": user.email,
            "id": user.id,
            "role": UserRoleEnum.USER.value
        }
        
        access_token = create_access_token(token_data)
        response.set_cookie(
            key="access_token",
            value=access_token,
            httponly=True,
            secure=True,
            samesite="lax"
        )

        return {"message": "User logged in"}
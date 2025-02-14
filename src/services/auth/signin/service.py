from decorators.create_session import create_session
from sqlmodel import Session, select
from models.user import User
from fastapi import HTTPException, Response
import jwt
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

        user_identifier = SignInService.create_token(user)

        response.set_cookie(key="access_token", value=user_identifier)

        return {"message": "User logged in"}
    
    @staticmethod
    def create_token(user: User) -> dict:
        encoded_jwt = jwt.encode({"user_email": user.email, "user_id": user.id, "role": "USER"}, "secret", algorithm="HS256")
        
        return encoded_jwt
from decorators.create_session import create_session
from sqlmodel import Session, select
from models.user import User
from fastapi import HTTPException, Response
import jwt
from enums.roles import UserRoleEnum

class SignUpService:

    @staticmethod
    @create_session
    def signup(session: Session, email: str, password: str, name: str, response= Response) -> str:
        query = select(User).where(User.email == email)

        user = session.exec(query).first()
        
        if user:
            raise HTTPException(status_code=400, detail="User already exists")

        user = User(email=email, password=password, name=name)
        
        session.add(user)
        session.commit()

        query = select(User.id).where(User.email == email)

        user_id = session.exec(query).first()

        user_identifier = SignUpService.create_token(user_email=email, user_id=user_id)

        response.set_cookie(key="access_token", value=user_identifier)

        return {"message": "User created"}
    
    @staticmethod
    def create_token(user_email: str, user_id: str) -> str:
        encoded_jwt = jwt.encode(payload={"email": user_email, "id": user_id, "role": "USER"}, key="MINHASENHASECRETA", algorithm="HS256")

        return encoded_jwt
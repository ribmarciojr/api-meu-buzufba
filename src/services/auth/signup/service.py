from decorators.create_session import create_session
from sqlmodel import Session, select
from models.user import User
from fastapi import HTTPException, Response
from config.jwt import create_access_token
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
        session.refresh(user)

        token_data = {
            "email": email,
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

        return {"message": "User created"}
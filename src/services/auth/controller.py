from fastapi import APIRouter, Request, Response
from .signin.schemas import SignInSchema
from .signup.schemas import SignUpSchema
from .signin.service import SignInService
from .signup.service import SignUpService
from .signout.service import SignoutService
import json


auth_router = APIRouter(prefix="/auth")

@auth_router.post("/signin")
def signin(user_payload: SignInSchema, response: Response):
    response = SignInService.signin(email=user_payload.email, password=user_payload.password, response=response)

    return response

@auth_router.post("/signup")
def signup(user_payload: SignUpSchema, response: Response):
    response = SignUpService.signup(email=user_payload.email, password=user_payload.password, name=user_payload.name, response=response)
    
    return response

@auth_router.get("/signout")
def signout(response: Response):
    response = SignoutService.signout(response)

    return response
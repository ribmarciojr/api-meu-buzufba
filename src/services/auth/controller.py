from fastapi import APIRouter
from .signin.schemas import SignInSchema
from .signin.service import SignInService
import json

auth_router = APIRouter(prefix="/auth")


@auth_router.post("/signin")
def signin(user_payload: SignInSchema):
    response = SignInService.sign_in(user_payload.email, user_payload.password)

    return json.dumps(response)


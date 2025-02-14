from fastapi import FastAPI
from sqlmodel import SQLModel
from fastapi.middleware.cors import CORSMiddleware
from models.user import User
from config.database import init_database
from services.auth.controller import auth_router

def create_app():
    app = FastAPI()
    origins = [
        "*",
        "http://localhost:3000",
    ]
    
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(auth_router)

    init_database()

    return app

app = create_app()
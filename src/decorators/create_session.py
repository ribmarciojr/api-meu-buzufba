from sqlmodel import Session
from config.database import engine
from functools import wraps

def create_session(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        with Session(engine) as session:
            return func(*args, session=session, **kwargs)
    return wrapper

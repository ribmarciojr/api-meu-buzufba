from sqlmodel import SQLModel, create_engine, Session
from models.user import User

DATABASE_URL = "sqlite3:///users.db"  


engine = create_engine(DATABASE_URL, echo=True)

def init_database():
    from sqlmodel import SQLModel

    SQLModel.metadata.create_all(engine)

    return engine

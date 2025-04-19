from contextlib import contextmanager, asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

sqlite_file_name = "library.db"
sqlite_url = f"sqlite:///db/{sqlite_file_name}"
engine = create_engine(sqlite_url, echo=True)


def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db()
    yield
    print("Shut down Library App")



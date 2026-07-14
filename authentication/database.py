from typing import Annotated

from fastapi import Depends
from sqlmodel import Session, SQLModel, create_engine

engine = create_engine("sqlite:///auth.db")


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

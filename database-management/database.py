from sqlmodel import create_engine

DATABASE_URL = "sqlite:///movies.db"

engine = create_engine(DATABASE_URL, echo=True)

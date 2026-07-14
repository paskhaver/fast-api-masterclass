from sqlmodel import Field, SQLModel

SQLModel.metadata.naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


class Movie(SQLModel, table=True):
    __tablename__: str = "movies"

    id: int | None = Field(default=None, primary_key=True)
    title: str
    in_theaters: bool = False

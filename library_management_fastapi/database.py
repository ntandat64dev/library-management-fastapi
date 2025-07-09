from os import environ as env

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

DATABASE_HOST = env.get("DATABASE_HOST", "localhost")
DATABASE_PORT = env.get("DATABASE_PORT", "5432")
DATABASE_NAME = env.get("DATABASE_NAME", "librarydb")
DATABASE_USERNAME = env.get("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = env.get("DATABASE_PASSWORD", "postgres")
DATABASE_URI = (
    "postgresql+psycopg2://{username}:{password}@{host}:{port}/{db_name}".format(
        username=DATABASE_USERNAME,
        password=DATABASE_PASSWORD,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        db_name=DATABASE_NAME,
    )
)

engine = create_engine(DATABASE_URI, echo=True)


class Base(DeclarativeBase):
    pass

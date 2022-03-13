import os

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_USER = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_NAME = os.environ.get("POSTGRES_NAME")

engine = create_engine(f"postgresql://{DB_USER}:{DB_PASSWORD}@db/{DB_NAME}")
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()


class NewsModel(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, autoincrement=True)
    content = Column(String)

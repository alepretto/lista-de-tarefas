from logging import root
from pathlib import Path
import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

root_path = Path(__file__).resolve().parent.parent
load_dotenv(f"{root_path}/.env")


engine = create_engine(os.environ["DATABASE_URL"])

LocalSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    try:
        db = LocalSession()
        yield db

    finally:
        db.close()
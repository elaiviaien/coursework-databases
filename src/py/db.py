import os

from dotenv import load_dotenv
from sqlmodel import create_engine, Session

from models import *

load_dotenv()
engine_url = os.getenv("DATABASE_URL")
engine = create_engine(engine_url,
                       pool_size=10,
                       max_overflow=5,
                       pool_timeout=30,
                       pool_recycle=1800
                       )

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session
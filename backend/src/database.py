from sqlalchemy import create_engine
from .security import settings
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(settings.POSTGRES_URI)
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()
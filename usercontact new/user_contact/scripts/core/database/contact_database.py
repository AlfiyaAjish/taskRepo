from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# from scripts.config.application_config import POSTGRESQL_CONFIG

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Alfi%402821@localhost:1282/user_contact"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Function to get the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

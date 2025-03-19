from sqlalchemy import Column, Integer, String
from user_contact.scripts.core.database.contact_database import Base
from pydantic import BaseModel

# SQLAlchemy model (database schema)
class Contact(Base):
    __tablename__ = 'contacts'

    contact_id = Column(Integer, primary_key=True, index=True)
    contact_name = Column(String, index=True)
    user_email = Column(String, unique=True, index=True)
    phone_number = Column(String)


# Pydantic model for request (used for creating contact)
class ContactCreate(BaseModel):
    contact_name: str
    user_email: str
    phone_number: str

# Pydantic model for response (used by FastAPI)
class ContactResponse(BaseModel):
    contact_id: int
    contact_name: str
    user_email: str
    phone_number: str

    class Config:
        orm_mode = True  # Tells Pydantic to treat the SQLAlchemy model as a dict

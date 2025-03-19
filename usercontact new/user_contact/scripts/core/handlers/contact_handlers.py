# user_contact/scripts/core/handlers/contact_handlers.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from user_contact.scripts.core.services.contact_services import create_contact, search_contacts, delete_contact,get_all_contacts,export_contact_to_excel_service
from user_contact.scripts.core.database.contact_database import get_db
from user_contact.scripts.core.models.contact_models import ContactCreate, ContactResponse
import os
from user_contact.scripts.core.models.contact_models import Contact, ContactCreate

contact_router = APIRouter()

@contact_router.post("/contacts/", response_model=ContactResponse)
def create_contact_endpoint(contact: ContactCreate, db: Session = Depends(get_db)):
    # Pass the ContactCreate Pydantic model to the service function
    return create_contact(db=db, contact=contact)

@contact_router.get("/contacts/", response_model=List[ContactResponse])
def get_all_contacts_endpoint(db: Session = Depends(get_db)):
    # Retrieve and return all contacts
    return get_all_contacts(db=db)



@contact_router.get("/contacts/{contact_id}", response_model=ContactResponse)
def search_contact_by_id_endpoint(contact_id: int, db: Session = Depends(get_db)):
    contact = search_contacts(db=db, contact_id=contact_id)
    return contact

@contact_router.delete("/contacts/{contact_id}", response_model=dict)
def delete_contact_endpoint(contact_id: int, db: Session = Depends(get_db)):
    success = delete_contact(db=db, contact_id=contact_id)
    if not success:
        raise HTTPException(status_code=404, detail="Contact not found")
    return {"message": "Contact deleted successfully"}


@contact_router.get("/contacts/excel/{email_id}")
def export_contact_to_excel_handler(email_id: str, db: Session = Depends(get_db)):
    # Call the service function to export contact data to Excel
    file_path = export_contact_to_excel_service(email_id, db)

    if file_path is None:
        raise HTTPException(status_code=404, detail="Contact not found")

    return {"message": f"Contact details have been exported to {file_path}"}




from sqlalchemy.orm import Session
from user_contact.scripts.core.models.contact_models import Contact, ContactCreate
from fastapi import HTTPException
from user_contact.scripts.utilities.mqtt_publisher import publish_mqtt_message
import pandas as pd
import os

def create_contact(db: Session, contact: ContactCreate):
    # Create the new contact instance and add it to the database
    db_contact = Contact(
        contact_name=contact.contact_name,
        user_email=contact.user_email,
        phone_number=contact.phone_number
    )
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact  # Return the created contact (SQLAlchemy model)

def get_all_contacts(db: Session):
    # Retrieve all contacts from the database
    contacts = db.query(Contact).all()
    return contacts  # Return the list of contacts (SQLAlchemy models)

def search_contacts(db: Session, contact_id: int):
    # Search for a contact by its contact_id
    contact = db.query(Contact).filter(Contact.contact_id == contact_id).first()

    if not contact:
        raise HTTPException(status_code=404, detail="Contact not found")

    return contact

def delete_contact(db: Session, contact_id: int):
    # Find and delete the contact by ID
    db_contact = db.query(Contact).filter(Contact.contact_id == contact_id).first()
    if db_contact:
        db.delete(db_contact)
        db.commit()
        return True
    return False

def export_contact_to_excel_service(email_id: str, db: Session):
    # Fetch contact by email
    contact = db.query(Contact).filter(Contact.user_email == email_id).first()

    if contact is None:
        return None

    # Prepare data for Excel
    data = {
        'Contact ID': [contact.contact_id],
        'Contact Name': [contact.contact_name],
        'User Email': [contact.user_email],
        'Phone Number': [contact.phone_number]
    }

    df = pd.DataFrame(data)

    # Set file path for Excel
    file_path = "user_contact_details.xlsx"

    # Check if the file already exists
    if os.path.exists(file_path):
        # If the file exists, load the existing data
        existing_df = pd.read_excel(file_path, engine='openpyxl')
        # Append new data to the existing DataFrame
        updated_df = pd.concat([existing_df, df], ignore_index=True)
        # Write the updated data back to the Excel file without overwriting existing data
        updated_df.to_excel(file_path, index=False, engine='openpyxl')
    else:
        # If the file doesn't exist, create a new file and add the current contact's data
        df.to_excel(file_path, index=False, engine='openpyxl')

    # Publish MQTT message
    publish_mqtt_message()

    return file_path
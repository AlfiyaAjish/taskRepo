from fastapi import FastAPI
from user_contact.scripts.core.handlers.contact_handlers import contact_router
from user_contact.scripts.core.handlers import user_handlers

def app():
    app = FastAPI()
    app.include_router(contact_router, prefix="/contact", tags=["Contact Service"])
    app.include_router(user_handlers.user_router, prefix="/user", tags=["User Service"])
    return app
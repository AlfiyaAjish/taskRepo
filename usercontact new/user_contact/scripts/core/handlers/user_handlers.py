from fastapi import APIRouter, HTTPException
from user_contact.scripts.core.services.user_services import (
    create_user,
    list_users,
    search_user,
    delete_user
)
from user_contact.scripts.core.models.models import User

user_router = APIRouter()

@user_router.post("/users/")
def create_new_user(user: User):
    result = create_user(user)
    return {"message": result}

@user_router.get("/users/")
def get_users():
    return {"users": list_users()}

@user_router.get("/users/{user_id}")
def get_user(user_id: str):
    user = search_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"user": user}

@user_router.delete("/users/{user_id}")
def delete_existing_user(user_id: str):
    result =  delete_user(user_id)
    if result:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

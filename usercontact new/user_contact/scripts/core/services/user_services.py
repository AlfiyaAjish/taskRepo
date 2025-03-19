from user_contact.scripts.core.database.database import db
from user_contact.scripts.core.models.models import User
from user_contact.scripts.constants.application_constants import USER_CREATED, USER_DELETED, USER_NOT_FOUND
from bson import ObjectId
from user_contact.scripts.core.validation.email_validation import is_valid_email
from user_contact.scripts.core.validation.phone_validation import is_valid_phone_number


def create_user(user: User):
    # Validate email
    if not is_valid_email(user.email):
        raise ValueError(f"Invalid email address: {user.email}")

    # Validate phone number
    if not is_valid_phone_number(user.phone_number):
        raise ValueError(f"Invalid phone number: {user.phone_number}")

    # Convert user Pydantic model to dictionary, excluding unset fields
    user_dict = user.dict(exclude_unset=True)

    # Insert user into MongoDB collection and get the result
    result = db.users.insert_one(user_dict)

    # Fetch the newly inserted user with the generated _id
    user_with_id = db.users.find_one({"_id": result.inserted_id})

    # Convert the result to the User model (this will automatically map _id to id)
    created_user = User(
        id=str(user_with_id["_id"]),  # Convert ObjectId to string
        name=user_with_id["name"],
        email=user_with_id["email"],
        phone_number=user_with_id["phone_number"]
    )

    # Return success message and the user object
    return USER_CREATED, created_user


def list_users():
    try:
        users_cursor = db.users.find({})  # Find all users synchronously
        users = []

        # Iterate over the cursor
        for user in users_cursor:
            # Check if user has '_id' and convert it to string
            if '_id' in user:
                users.append({
                    "id": str(user["_id"]),  # Convert MongoDB ObjectId to string
                    "name": user.get("name"),
                    "email": user.get("email"),
                    "phone_number": user.get("phone_number")
                })
            else:
                # Log or handle the case where _id is not found (although this shouldn't happen)
                print("User without _id found:", user)

        return {"users": users}

    except Exception as e:
        # Log the error if there's any issue
        print(f"Error fetching users: {e}")
        return {"error": str(e)}


def search_user(user_id: str):
    user = db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        # Manually map '_id' to 'id' and pass it to User model
        user_data = {
            "id": str(user['_id']),  # Convert MongoDB ObjectId to string and map to 'id'
            "name": user.get('name'),
            "email": user.get('email'),
            "phone_number": user.get('phone_number')
        }
        return User(**user_data)
    return None

def delete_user(user_id: str):
    result = db.users.delete_one({"_id": ObjectId(user_id)})
    if result.deleted_count:
        return USER_DELETED
    return USER_NOT_FOUND

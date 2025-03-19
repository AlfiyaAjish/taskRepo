from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    phone_number: str
class UserInDB(User):
    id: str
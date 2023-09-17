from pydantic import BaseModel

# Base class
class UserBase(BaseModel):
    email: str
    first_name: str
    last_name: str
    latitude: str
    longitude: str
    user_image: str
    phone_number: str

# Class for creating new row
class UserCreate(UserBase):
    middle_name: str | None = None
    hashed_password: str
    dob: str | None = None
    

# Class for reading data from db
class User(UserBase):
    id: int
    middle_name: str | None = None
    dob: str | None = None


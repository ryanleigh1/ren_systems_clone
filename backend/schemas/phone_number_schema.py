from enum import Enum

from pydantic import BaseModel


class PhoneType(str, Enum):
    """
    Enum for phone types.
    """
    personal = "personal"
    work = "work"
    mobile = "mobile"

class PhoneNumberRead(BaseModel):
    id: int
    phone_number: str
    type: PhoneType

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models

class PhoneNumberCreate(BaseModel):
    id: int
    phone_number: str
    type: PhoneType

class PhoneNumberUpdate(BaseModel):
    id: int
    phone_number: str
    type: PhoneType

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models
from enum import Enum
from typing import Optional

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
    id: Optional[int] = None
    contact_id: int
    phone_number: str
    type: PhoneType

    class Config:
        orm_mode = True

class PhoneNumberUpdate(BaseModel):
    phone_number: str
    type: PhoneType

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models

class PhoneNumberDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models
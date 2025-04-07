from datetime import date
from enum import Enum
from pydantic import BaseModel
from typing import Optional, List

from schemas.phone_number_schema import PhoneType

class EmailType(str, Enum):
    """
    Enum for email types.
    """
    personal = "personal"
    work = "work"

class EmailUpdate(BaseModel):
    id: Optional[int]  # Optional for new emails
    email_address: str
    type: EmailType
    
class WebInfoType(str, Enum):
    """
    Enum for web info types.
    """
    personal = "personal"
    work = "work"
    linkedin = "linkedin"


class WebInfoUpdate(BaseModel):
    id: Optional[int]  # Optional for new web info
    url: str
    type: WebInfoType
    
class ContactPhoneNumber(BaseModel):
    id: int
    phone_number: str
    type: PhoneType

    class Config:
        orm_mode = True
        
class ContactEmail(BaseModel):
    """
    Pydantic model for Contact Email.
    """
    id: int
    email_address: str
    type: EmailType

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models
        
class ContactWebInfo(BaseModel):
    """
    Pydantic model for Contact Web Info.
    """
    id: int
    url: str
    type: WebInfoType

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    date_of_birth: Optional[date] = None  # Use str for simplicity, can be changed to date if needed
    is_vip: Optional[bool] = False
    
class ContactRead(ContactBase):
    id: int
    email_addresses: Optional[List[ContactEmail]] = []
    phone_numbers: Optional[List[ContactPhoneNumber]] = []
    web_info: Optional[List[ContactWebInfo]] = []
    
    class Config:
        orm_mode = True
        
class ContactCreate(ContactBase):
    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models
  
class ContactUpdate(ContactBase):
    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models
        
class ContactDelete(ContactBase):
    id: int  # Ensure we have the ID of the contact to delete

    class Config:
        orm_mode = True  # Allows ORM objects to be serialized into Pydantic models
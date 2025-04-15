from datetime import date
from enum import Enum
from pydantic import BaseModel
from pydantic.alias_generators import to_camel
from typing import Optional, List

from schemas.email_schema import EmailType
from schemas.phone_number_schema import PhoneType
    
class WebInfoType(str, Enum):
    """
    Enum for web info types.
    """
    personal = "personal"
    work = "work"
    linkedin = "linkedin"

class ContactBase(BaseModel):
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    date_of_birth: Optional[date] = None  # Use str for simplicity, can be changed to date if needed
    is_vip: Optional[bool] = False

    model_config = {
        "from_attributes": True,
        "alias_generator": to_camel,
        "populate_by_name": True,
    }

class WebInfoUpdate(BaseModel):
    id: Optional[int]  # Optional for new web info
    url: str
    type: WebInfoType
    
class ContactPhoneNumber(BaseModel):
    id: int
    phone_number: str
    type: PhoneType
        
class ContactEmail(BaseModel):
    id: int
    email_address: str
    type: EmailType

    model_config = {
        "from_attributes": True,
        "alias_generator": to_camel,
        "populate_by_name": True,
    }
        
class ContactWebInfo(BaseModel):
    id: int
    url: str
    type: WebInfoType

    model_config = {
        "from_attributes": True,
        "alias_generator": to_camel,
        "populate_by_name": True,
    }
    
class ContactRead(ContactBase):
    id: int
    email_addresses: Optional[List[ContactEmail]] = []
    phone_numbers: Optional[List[ContactPhoneNumber]] = []
    web_info: Optional[List[ContactWebInfo]] = []
        
class ContactCreate(ContactBase):
    pass
  
class ContactUpdate(ContactBase):
    pass
        
class ContactDelete(ContactBase):
    id: int  # Ensure we have the ID of the contact to delete
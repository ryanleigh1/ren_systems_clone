from enum import Enum
from typing import Optional

from pydantic import BaseModel


class EmailType(Enum):
    personal = "personal"
    work = "work"

class EmailRead(BaseModel):
    id: int
    email_address: str
    type: EmailType

    class Config:
        orm_mode = True

class EmailCreate(BaseModel):
    contact_id: int
    email_address: str
    type: EmailType

    class Config:
        orm_mode = True

class EmailUpdate(BaseModel):
    id: Optional[int]
    email_address: str
    type: EmailType

    class Config:
        orm_mode = True

class EmailDelete(BaseModel):
    id: int

    class Config:
        orm_mode = True
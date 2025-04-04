from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud.contact import get_contacts_with_details
from schemas.schemas import ContactRead  # Import Pydantic schemas
from db import get_db  # Import your DB session dependency

router = APIRouter()

@router.get("/contacts", response_model=list[ContactRead])
async def get_contacts(db: AsyncSession = Depends(get_db)):
    try:
        contacts = await get_contacts_with_details(db)  # Call the function to get contacts with details        
        return contacts  # Return the list of contacts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
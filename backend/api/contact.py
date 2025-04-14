from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud.contact import get_contacts_with_details
from crud.contact import update_contact  # Import the update function from CRUD
from backend.schemas.contact_schema import ContactRead, ContactUpdate  # Import Pydantic schemas
from db import get_db

router = APIRouter()

@router.get("/contacts", response_model=list[ContactRead])
async def get_contacts(db: AsyncSession = Depends(get_db)):
    try:
        contacts = await get_contacts_with_details(db)  # Call the function to get contacts with details        
        return contacts  # Return the list of contacts
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.patch("/contacts/{contact_id}", response_model=ContactUpdate)
async def patch_contact(contact_id: int, request_body: ContactUpdate, db: AsyncSession = Depends(get_db)):
    """
    Endpoint to update a contact.
    """
    try:
        # Call the update function from CRUD
        updated_contact = await update_contact(contact_id=contact_id, request_body=request_body, db=db)
        
        if not updated_contact:
            raise HTTPException(status_code=404, detail="Contact not found")
        
        return updated_contact  # Return the updated contact
    except Exception as e:
      if isinstance(e, HTTPException):
        raise e
      raise HTTPException(status_code=500, detail=str(e)) from e

from sqlalchemy.future import select
from sqlalchemy.sql import Update
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from schemas.schemas import ContactUpdate
from models import Contact


async def get_contacts_with_details(db: AsyncSession):
    stmt = (
        select(Contact)
        .options(
            selectinload(Contact.email_addresses),
            selectinload(Contact.phone_numbers),
            selectinload(Contact.web_info),
        )
    )
    
    result = await db.execute(stmt)  # Async execution
    return result.scalars().all()  # Extract first result

async def get_contact_with_details(db: AsyncSession, contact_id: int):
    stmt = (
        select(Contact)
        .where(Contact.id == contact_id)
        .options(
            joinedload(Contact.email_addresses),
            joinedload(Contact.phone_numbers),
            joinedload(Contact.web_info),
        )
    )
    
    result = await db.execute(stmt)  # Async execution
    return result.scalars().first()  # Extract first result
  
async def create_contact(contact: Contact, db: AsyncSession):
  db.add(contact)  # Add the new contact to the session
  try:
    await db.commit()  # Commit the transaction to save the new contact
  except Exception as e:
    await db.rollback()  # Rollback in case of an error
    raise e  # Re-raise the exception for handling upstream

async def update_contact(contact_id: int, request_body: ContactUpdate, db: AsyncSession):
    stmt = (
      Update(Contact)
        .where(Contact.id == contact_id)
        .values(**request_body.model_dump(exclude_unset=True))  # Use exclude_unset to avoid sending None values
        .execution_options(synchronize_session='fetch')
    )
    
    result = await db.execute(stmt)  # Async execution
    await db.commit()  # Commit the transaction to save changes
    
    if result.rowcount == 0:
        return None
    # If the update was successful, return the updated contact
    updated_contact = await db.get(Contact, contact_id)
    return updated_contact
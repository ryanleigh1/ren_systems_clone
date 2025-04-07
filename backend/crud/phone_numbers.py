from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import Update

from schemas.phone_number_schema import PhoneNumberUpdate
from models import ContactPhoneNumbers



async def get_phone_numbers(contact_id: int, db: AsyncSession):
    """
    Get all phone numbers for a specific contact.
    """
    stmt = (
        select(ContactPhoneNumbers)
        .where(ContactPhoneNumbers.id == contact_id)
    )
    
    result = await db.execute(stmt)  # Async execution
    return result.scalars().all()

async def update_phone_number(id: int, request_body: PhoneNumberUpdate, db: AsyncSession):
    """
    Update a specific phone number.
    """
    stmt = (Update(ContactPhoneNumbers)
      .where(ContactPhoneNumbers.id == id)
      .values(**request_body.model_dump(exclude_unset=True))  # Use exclude_unset to avoid sending None values
      .execution_options(synchronize_session='fetch')
    )

    result = await db.execute(stmt)  # Async execution
    await db.commit()

    if result.rowcount == 0:
        return None
    return await db.get(ContactPhoneNumbers, id)
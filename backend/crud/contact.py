from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from models import Contact

import logging
from sqlalchemy.engine import Engine

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


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
        .options(
            joinedload(Contact.email_addresses),
            joinedload(Contact.phone_numbers),
            joinedload(Contact.web_info),
        )
        .filter(Contact.id == contact_id)
    )
    
    result = await db.execute(stmt)  # Async execution
    return result.scalars().first()  # Extract first result

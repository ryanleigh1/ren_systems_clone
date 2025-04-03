from sqlalchemy.future import select
from sqlalchemy.orm import joinedload
from sqlalchemy.ext.asyncio import AsyncSession
from models import Contact

import logging
from sqlalchemy.engine import Engine

logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)



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
    
    logging.info(f"Executing query: {stmt}")  # Log query
    logging.info(f"With parameters: {contact_id}")  # Log parameters
    
    result = await db.execute(stmt)  # Async execution
    return result.scalars().first()  # Extract first result

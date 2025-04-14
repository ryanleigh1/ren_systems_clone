from sqlalchemy import Update, delete, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.models import ContactEmails
from backend.schemas.email_schema import EmailCreate, EmailUpdate

async def get_email_addresses(contact_id: int, db: AsyncSession):
  stmt = (
      select(ContactEmails)
      .where(contact_id = ContactEmails.contact_id)
    )

  result = await db.execute(stmt)
  return result.scalars.all()

async def create_email_address(request_body: EmailCreate, db: AsyncSession):
  new_email = ContactEmails(**request_body.model_dump())
  db.add(new_email)
  await db.commit()
  await db.refresh(new_email)

  return new_email

async def update_email_address(id: int, request_body: EmailUpdate, db: AsyncSession):
  stmt = (
    Update(ContactEmails)
    .where(ContactEmails.id == id)
    .values(**request_body.model_dump(exclude_unset=True))
    .execution_options(synchronize_session="fetch")
  )
  result = await db.execute(stmt)
  await db.commit()

  if result.rowcount == 0: return None

  return await db.get(ContactEmails, id)

async def remove_email_address(id: int, db: AsyncSession):
  stmt = delete(ContactEmails).where(ContactEmails.id == id)

  result = await db.execute(stmt)
  await db.commit()

  if result.rowcount == 0: return None
  return {"message": f"Email with ID {id} deleted."}
  
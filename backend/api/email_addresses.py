from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from backend.crud.email_addresses import create_email_address, get_email_addresses, remove_email_address, update_email_address
from backend.schemas.email_schema import EmailCreate, EmailRead, EmailUpdate
from db import get_db

router = APIRouter()

@router.get("/emails", response_model=list[EmailRead])
async def get_emails(contact_id: int, db: AsyncSession = Depends(get_db)):
  try:
    emails = await get_email_addresses(contact_id, db)
    return emails
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

@router.post("/emails", response_model=EmailRead)
async def post_email(request_body: EmailCreate, db: AsyncSession):
  try:
    new_email = await create_email_address(request_body, db)
    return new_email
  except Exception as e:
    if isinstance(e, HTTPException):
        raise e
    raise HTTPException(status_code=500, detail=str(e)) from e

@router.patch("/emails/{id}", response_model=EmailRead)
async def patch_email(id: int, request_body: EmailUpdate, db: AsyncSession):
  try:
    updated_email = await update_email_address(id, request_body, db)

    if not updated_email:
      raise HTTPException(status_code=404, detail="Email not found")
    return updated_email
  except Exception as e:
    if isinstance(e, HTTPException):
      raise e
    raise HTTPException(status_code=500, detail=str(e)) from e

@router.delete("/emails/{id}", response_model=None)
async def delete_email(id: int, db: AsyncSession):
  try:
    msg = await remove_email_address(id, db)
    return msg
  except Exception as e:
    if isinstance(e, HTTPException):
        raise e
    raise HTTPException(status_code=500, detail=str(e)) from e
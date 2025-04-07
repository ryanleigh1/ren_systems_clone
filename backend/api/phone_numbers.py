from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud.phone_numbers import get_phone_numbers, update_phone_number
from schemas.phone_number_schema import PhoneNumberRead, PhoneNumberUpdate
from db import get_db

router = APIRouter()

@router.get("/contact_phone_numbers", response_model=list[PhoneNumberRead])
async def fetch_phone_numbers(contact_id: int, db: AsyncSession = Depends(get_db)):
  try:
    phone_numbers = await get_phone_numbers(contact_id=contact_id, db=db)
    return phone_numbers
  except Exception as e:
      if isinstance(e, HTTPException):
        raise e
      raise HTTPException(status_code=500, detail=str(e)) from e

@router.patch("/contact_phone_numbers/{phone_number_id}", response_model=PhoneNumberUpdate)
async def patch_phone_number(phone_number_id: int, request_body: PhoneNumberUpdate, db: AsyncSession = Depends(get_db)):
    try:
      updated_phone_number = await update_phone_number(id=phone_number_id, request_body=request_body, db=db)

      if not updated_phone_number:
          raise HTTPException(status_code=404, detail="Phone number not found")
      return updated_phone_number
    except Exception as e:
      if isinstance(e, HTTPException):
        raise e
      raise HTTPException(status_code=500, detail=str(e)) from e
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from crud.phone_numbers import create_phone_number, get_phone_numbers, remove_phone_number, update_phone_number
from schemas.phone_number_schema import PhoneNumberCreate, PhoneNumberDelete, PhoneNumberRead, PhoneNumberUpdate
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

@router.post("/contact_phone_numbers", response_model=PhoneNumberRead)
async def post_phone_number(request_body: PhoneNumberCreate, db: AsyncSession = Depends(get_db)):
    try:
        new_phone_number = await create_phone_number(request_body=request_body, db=db)
        return new_phone_number
    except Exception as e:
      if isinstance(e, HTTPException):
        raise e
      raise HTTPException(status_code=500, detail=str(e)) from e

@router.patch("/contact_phone_numbers/{phone_number_id}", response_model=PhoneNumberRead)
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

@router.delete("/contact_phone_numbers/{phone_number_id}", response_model=None)
async def delete_phone_number(phone_number_id: int, db: AsyncSession = Depends(get_db)):
    try:
        msg = await remove_phone_number(id=phone_number_id, db=db)
        return msg
    except Exception as e:
      if isinstance(e, HTTPException):
        raise e
      raise HTTPException(status_code=500, detail=str(e)) from e
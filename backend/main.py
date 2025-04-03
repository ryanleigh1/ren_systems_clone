from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from models import Contact
from db import get_db
from crud.contact import get_contact_with_details


app = FastAPI()

@app.get("/")
async def home():
    return {"message": "FastAPI is running!"}

# Test database connection
@app.get("/test-db")
async def test_db_connection(db: AsyncSession = Depends(get_db)):
    try:
        # Execute a simple query
        result = await db.execute(text("SELECT 1"))
        return {"message": "Database connected successfully!", "result": result.scalar()}
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/contacts")
async def get_contacts(db: AsyncSession = Depends(get_db)):
    try:
        # Use SQLAlchemy ORM to query the `Contact` table
        query = select(Contact)  # Make sure you import Contact model
        result = await db.execute(query)
        contacts = result.scalars().all()  # Fetch all records
        
        if not contacts:
            return {"message": "No contacts found."}
        return {"contacts": contacts}
    except Exception as e:
        return {"error": str(e)}

@app.get("/contact/{contact_id}")
async def get_contact(contact_id: int, db: AsyncSession = Depends(get_db)):
    contact = await get_contact_with_details(db, contact_id)
    if not contact:
        return {"error": "Contact not found"}

    return {
        "id": contact.id,
        "name": f"{contact.first_name} {contact.last_name}",
        "emails": [email.email for email in contact.email_addresses],
        "phone_numbers": [{"number": p.phone_number, "type": p.type.value} for p in contact.phone_numbers],
        "web_info": [web.url for web in contact.web_info],
    }
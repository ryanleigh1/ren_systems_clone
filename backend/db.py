from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# DATABASE_URL = os.getenv("DATABASE_URL", )
# DATABASE_URL = "postgresql+asyncpg://postgres:420Sorrey!6969@db.gwtcovqsljrcthksmsar.supabase.co:5432/postgres"
DATABASE_URL = "postgresql+asyncpg://postgres.gwtcovqsljrcthksmsar:420Sorrey!6969@aws-0-us-east-1.pooler.supabase.com:5432/postgres"
# Create async engine and session
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Dependency to get DB session
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

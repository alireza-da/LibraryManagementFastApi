from sqlalchemy.ext.asyncio import async_session

from db.database import SessionLocal
from typing import Generator, AsyncGenerator


def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


async def get_db_async() -> AsyncGenerator:
    async with async_session() as session:
        yield session

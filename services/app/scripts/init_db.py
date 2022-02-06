import asyncio
import logging
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession
from dotenv import load_dotenv

from src.python.app.core.config import settings
from src.python.app.core.database import SessionLocal
from src.python.app.core.security import get_password_hash
from src.python.app.models.users import User

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def create_first_user(session: AsyncSession) -> None:
    email = settings.FIRST_USER_EMAIL
    password = get_password_hash(settings.FIRST_USER_PASSWORD.get_secret_value())
    user = User(email=email, hashed_password=password, is_superuser=True)
    try:
        session.add(user)
    except IntegrityError:
        logger.info("Superuser already exists")

async def main():
    logger.info("Creating initial data")
    async with SessionLocal() as session:
        await create_first_user(session)
    logger.info("Initial data created")

if __name__ == "__main__":
    asyncio.run(main())
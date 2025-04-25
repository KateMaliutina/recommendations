import os

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine  # sync-подключение
from dotenv import load_dotenv

# from app.models import Base

load_dotenv()

# Загружаем переменные окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost/recommendations")

# Создаём асинхронный движок и фабрику сессий (для FastAPI)
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

# Синхронный движок (для Alembic и ProcessPoolExecutor)
sync_db_url = DATABASE_URL.replace("asyncpg", "psycopg2")
sync_engine = create_engine(sync_db_url, echo=True)
SessionLocal = sessionmaker(bind=sync_engine)


# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

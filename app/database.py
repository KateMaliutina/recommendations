from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
# from app.models import Base

load_dotenv()

# Загружаем переменные окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost/recommendations")

# Создаём асинхронный движок для подключения к БД
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаём фабрику сессий
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # todo make sure it works


# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

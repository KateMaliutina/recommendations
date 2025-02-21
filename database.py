from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
import os

# Загружаем переменные окружения (можно вынести в .env)
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:postgres@localhost/recommendations")  # todo use envs

# Создаём асинхронный движок для подключения к БД
engine = create_async_engine(DATABASE_URL, echo=True)

# Создаём фабрику сессий
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)  # todo make sure it works


# Функция для получения сессии
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

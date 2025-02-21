import asyncio
from database import engine
from models import Base


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


if __name__ == "__main__":  # todo test in docker without script
    asyncio.run(init_db())

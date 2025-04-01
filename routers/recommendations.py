from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from recommendation import get_recommendations

router = APIRouter()


@router.get("/recommendations/{user_id}")
async def get_user_recommendations(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_recommendations(user_id, db)

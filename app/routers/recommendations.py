from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.recommendation import get_recommendations

router = APIRouter()


@router.get("/get/{user_id}")
async def get_user_recommendations(user_id: int, db: AsyncSession = Depends(get_db)):
    return await get_recommendations(user_id, db)

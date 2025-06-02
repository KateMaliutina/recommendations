from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.recommendation import get_recommendations

router = APIRouter()


@router.get("/get/{user_id}")
async def get_user_recommendations(
        user_id: int,
        page: int = Query(1, ge=1, description="Номер страницы (по умолчанию 1)"),
        page_size: int = Query(10, ge=1, le=50, description="Количество вакансий на странице (по умолчанию 10)"),
        db: AsyncSession = Depends(get_db)
):
    return await get_recommendations(user_id=user_id, db=db, page=page, page_size=page_size)

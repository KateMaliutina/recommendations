from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from database import get_db
from crud import create_skill, get_skills
from pydantic import BaseModel

router = APIRouter()


# Pydantic-модель для валидации
class SkillCreate(BaseModel):
    name: str


# Эндпоинт для создания навыка
@router.post("/skills/")
async def add_skill(skill: SkillCreate, db: AsyncSession = Depends(get_db)):
    return await create_skill(db, skill.name)


# Эндпоинт для получения всех навыков
@router.get("/skills/")
async def list_skills(db: AsyncSession = Depends(get_db)):
    return await get_skills(db)

from fastapi import APIRouter, Depends
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.crud import get_users
from pydantic import BaseModel
from typing import List

from app.models import User, UserSkill, Skill

router = APIRouter()


class SkillCreate(BaseModel):
    name: str
    level: int  # Уровень владения навыком (например, от 1 до 100)


# Pydantic-модель для валидации
class UserCreate(BaseModel):
    name: str
    email: str
    level: str
    interests: List[str]
    skills: List[SkillCreate]  # Список навыков пользователя


# Эндпоинт для создания пользователя
@router.post("/users/")
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Создание пользователя с привязкой переданных навыков и уровней владения.
    """
    # Создаем нового пользователя
    new_user = User(name=user.name, email=user.email, level=user.level, interests=user.interests)
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)  # Получили сгенерированный ID

    # Обрабатываем навыки пользователя
    for skill_item in user.skills:
        skill_name = skill_item.name.lower()
        proficiency_level = skill_item.level

        # Проверяем, есть ли такой навык в базе
        result = await db.execute(select(Skill).where(Skill.name == skill_name))
        existing_skill = result.scalar_one_or_none()
        if not existing_skill:
            await db.commit()
            existing_skill = Skill(name=skill_name)
            db.add(existing_skill)
            await db.commit()
            await db.refresh(existing_skill)

        # Создаем связь пользователя с навыком
        user_skill = UserSkill(user_id=new_user.id, skill_id=existing_skill.id, proficiency_level=proficiency_level)
        db.add(user_skill)

    await db.commit()
    return new_user
    # return await create_user(db, user.name, user.email, user.level, user.interests)


# Эндпоинт для получения всех пользователей
@router.get("/users/")
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)

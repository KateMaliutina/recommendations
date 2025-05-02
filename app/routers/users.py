from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import delete
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.crud import get_users
from pydantic import BaseModel
from typing import List, Optional

from app.models import User, UserSkill, Skill

router = APIRouter()


class SkillCreate(BaseModel):
    name: str
    proficiency_level: int  # Уровень владения навыком (например, от 1 до 100)


# Pydantic-модель для валидации
class UserCreate(BaseModel):
    email: str
    name: Optional[str] = None
    grade: Optional[str] = None
    interests: Optional[List[str]] = None
    skills: Optional[List[SkillCreate]] = None  # Список навыков пользователя


class UserUpdate(BaseModel):
    email: str
    name: Optional[str] = None
    grade: Optional[str] = None
    interests: Optional[List[str]] = None
    skills: Optional[List[SkillCreate]] = None


# Эндпоинт для создания пользователя
@router.post("/users/")
async def add_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    """
    Создание пользователя с возможностью частичного заполнения профиля.
    Обязателен только email.
    """
    new_user = User(
        name=user.name,
        email=user.email,
        grade=user.grade,
        interests=user.interests
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)

    # Обработка навыков, если они переданы
    if user.skills:
        for skill_item in user.skills:
            skill_name = skill_item.name.lower()
            proficiency_level = skill_item.proficiency_level

            # Поиск существующего навыка
            result = await db.execute(select(Skill).where(Skill.name == skill_name))
            existing_skill = result.scalar_one_or_none()
            if not existing_skill:
                existing_skill = Skill(name=skill_name)
                db.add(existing_skill)
                await db.commit()
                await db.refresh(existing_skill)

            # Связываем пользователя с навыком
            user_skill = UserSkill(
                user_id=new_user.id,
                skill_id=existing_skill.id,
                proficiency_level=proficiency_level
            )
            db.add(user_skill)

        await db.commit()

    return {"data": new_user.id}


# Эндпоинт для получения всех пользователей
@router.get("/users/")
async def list_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)


@router.put("/users/{user_id}")
async def update_user(user_id: int, user: UserUpdate, db: AsyncSession = Depends(get_db)):
    """Обновление информации о пользователе и его навыках (частично)"""
    existing_user = await db.get(User, user_id)
    if not existing_user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Обновляем только переданные поля
    existing_user.email = user.email  # обязателен
    if user.name is not None:
        existing_user.name = user.name
    if user.grade is not None:
        existing_user.grade = user.grade
    if user.interests is not None:
        existing_user.interests = user.interests

    if user.skills is not None:
        # Удаляем старые навыки
        await db.execute(delete(UserSkill).where(UserSkill.user_id == user_id))

        # Добавляем новые
        for skill_item in user.skills:
            skill_name = skill_item.name.lower()
            proficiency_level = skill_item.proficiency_level

            result = await db.execute(select(Skill).where(Skill.name == skill_name))
            skill = result.scalar_one_or_none()
            if not skill:
                skill = Skill(name=skill_name)
                db.add(skill)
                await db.commit()
                await db.refresh(skill)

            user_skill = UserSkill(user_id=user_id, skill_id=skill.id, proficiency_level=proficiency_level)
            db.add(user_skill)

    await db.commit()
    await db.refresh(existing_user)
    return existing_user


@router.delete("/users/{user_id}")
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    """Удаление пользователя и его навыков"""
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    # Удаляем связанные UserSkill
    await db.execute(delete(UserSkill).where(UserSkill.user_id == user_id))

    await db.delete(user)
    await db.commit()

    return {"detail": f"Пользователь с ID {user_id} успешно удалён"}

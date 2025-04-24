from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Vacancy, Skill, UserSkill, VacancySkill, Recommendation


# Создание пользователя
async def create_user(db: AsyncSession, name: str, email: str, level: str, interests: list):
    user = User(name=name, email=email, level=level, interests=interests)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


# Получение пользователей
async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


# Добавление навыка
async def create_skill(db: AsyncSession, name: str):
    skill = Skill(name=name)
    db.add(skill)
    await db.commit()
    await db.refresh(skill)
    return skill


# Получение всех навыков
async def get_skills(db: AsyncSession):
    result = await db.execute(select(Skill))
    return result.scalars().all()


# Привязка навыка к пользователю
async def add_user_skill(db: AsyncSession, user_id: int, skill_id: int, proficiency_level: int):
    user_skill = UserSkill(user_id=user_id, skill_id=skill_id, proficiency_level=proficiency_level)
    db.add(user_skill)
    await db.commit()
    return user_skill


# Создание вакансии
async def create_vacancy(db: AsyncSession, title: str, description: str, level: str):
    vacancy = Vacancy(title=title, description=description, level=level)
    db.add(vacancy)
    await db.commit()
    await db.refresh(vacancy)
    return vacancy


# Получение пользователей
async def get_vacancies(db: AsyncSession):
    result = await db.execute(select(Vacancy))
    return result.scalars().all()


# Привязка навыка к вакансии
async def add_vacancy_skill(db: AsyncSession, vacancy_id: int, skill_id: int):
    vacancy_skill = VacancySkill(vacancy_id=vacancy_id, skill_id=skill_id)
    db.add(vacancy_skill)
    await db.commit()
    return vacancy_skill


# Создание рекомендации
async def create_recommendation(db: AsyncSession, user_id: int, vacancy_id: int, score: int):
    recommendation = Recommendation(user_id=user_id, vacancy_id=vacancy_id, score=score)
    db.add(recommendation)
    await db.commit()
    await db.refresh(recommendation)
    return recommendation

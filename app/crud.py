from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import User, Vacancy, Skill, UserSkill, VacancySkill, Recommendation


# Создание пользователя
async def create_user(db: AsyncSession, name: str, email: str, grade: str, interests: list, specialization: str):
    user = User(name=name, email=email, grade=grade, interests=interests, specialization=specialization)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


# Получение пользователей
async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()


# Получение пользователя
async def get_one_user(db: AsyncSession, user_id: int):
    return await db.get(User, user_id)


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
async def create_vacancy(db: AsyncSession, title: str, description: str, grade: str, employer_name: str, url: str):
    vacancy = Vacancy(title=title,
                      description=description,
                      grade=grade,
                      employer_name=employer_name,
                      url=url)
    db.add(vacancy)
    await db.commit()
    await db.refresh(vacancy)
    return vacancy


# Получение вакансий
async def get_vacancies(db: AsyncSession):
    result = await db.execute(select(Vacancy))
    return result.scalars().all()


# Получение вакансии
async def get_one_vacancy(db: AsyncSession, vacancy_id: int):
    return await db.get(Vacancy, vacancy_id)


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

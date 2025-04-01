from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models import User, Vacancy, UserSkill, VacancySkill, Recommendation
from collections import Counter


async def get_recommendations(user_id: int, db: AsyncSession):
    """ Генерация списка рекомендаций по вакансиям для пользователя """

    # Получаем данные пользователя
    user = await db.get(User, user_id)
    if not user:
        return {"error": "User not found"}

    # Получаем навыки пользователя
    user_skills = await db.execute(select(UserSkill).where(UserSkill.user_id == user_id))
    user_skills = {us.skill_id: us.proficiency_level for us in user_skills.scalars().all()}

    # Получаем все вакансии
    vacancies = await db.execute(select(Vacancy))
    vacancies = vacancies.scalars().all()

    recommendations = []

    for vacancy in vacancies:
        # Получаем требуемые навыки вакансии
        vacancy_skills = await db.execute(select(VacancySkill).where(VacancySkill.vacancy_id == vacancy.id))
        vacancy_skills = {vs.skill_id for vs in vacancy_skills.scalars().all()}

        # 1️⃣ Оценка совпадения навыков
        skill_match = sum([user_skills.get(skill, 0) for skill in vacancy_skills])

        # 2️⃣ Оценка соответствия уровня
        level_match = 10 if user.level == vacancy.level else -10

        # 3️⃣ Оценка интересов (по ключевым словам)
        interest_match = sum([1 for interest in user.interests if interest.lower() in vacancy.description.lower()])

        # Итоговый балл
        score = skill_match + level_match + interest_match * 5  # Учитываем веса

        recommendations.append({"vacancy_id": vacancy.id, "score": score})

    # Сортируем по убыванию score и ограничиваем топ-10 вакансий
    recommendations = sorted(recommendations, key=lambda x: x["score"], reverse=True)[:10]

    # Сохраняем в базу
    for rec in recommendations:
        recommendation = Recommendation(user_id=user_id, vacancy_id=rec["vacancy_id"], score=rec["score"])
        db.add(recommendation)

    await db.commit()
    return recommendations

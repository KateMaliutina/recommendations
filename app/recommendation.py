import http

from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models import User, Vacancy, UserSkill, VacancySkill, Recommendation


async def get_recommendations(user_id: int, db: AsyncSession, page: int = 1, page_size: int = 10):
    """
    Генерация списка рекомендаций по вакансиям для пользователя.
    Параметры:  user_id - идентификатор пользователя.
                page - номер страницы (по умолчанию 1).
                page_size - количество вакансий на странице (по умолчанию 10).
    """

    # Получаем данные пользователя
    user = await db.get(User, user_id)
    if not user:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Пользователь не найден")

    # Получаем навыки пользователя
    user_skills_result = await db.execute(select(UserSkill).where(UserSkill.user_id == user_id))
    user_skills = {us.skill_id: us.proficiency_level for us in user_skills_result.scalars().all()}

    # Получаем все вакансии
    vacancies_result = await db.execute(select(Vacancy))
    vacancies = vacancies_result.scalars().all()

    recommendations = []

    for vacancy in vacancies:
        # Получаем требуемые навыки вакансии
        vacancy_skills_result = await db.execute(select(VacancySkill).where(VacancySkill.vacancy_id == vacancy.id))
        vacancy_skills = {vs.skill_id for vs in vacancy_skills_result.scalars().all()}

        # 1. Оценка совпадения навыков
        skill_match = sum([user_skills.get(skill, 0) for skill in vacancy_skills])

        # 2. Оценка соответствия уровня
        grade_match = 10 if user.grade == vacancy.grade else -10

        # 3. Оценка интересов (по ключевым словам)
        interest_match = sum(
            [1 for interest in user.interests if interest.lower() in (vacancy.description or "").lower()])

        # Итоговый балл
        score = skill_match + grade_match + interest_match * 5  # Учитываем веса

        recommendations.append({"vacancy": vacancy, "score": score})

    # Сортируем по убыванию score
    recommendations.sort(key=lambda x: x["score"], reverse=True)

    # Пагинация
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    page_recommendations = recommendations[start_index:end_index]

    # Сохраняем только рекомендации для этой страницы
    for rec in page_recommendations:
        recommendation = Recommendation(user_id=user_id, vacancy_id=rec["vacancy"].id, score=rec["score"])
        db.add(recommendation)

    await db.commit()

    # Возвращаем вакансии с их итоговым score
    return [
        {
            "vacancy_id": rec["vacancy"].id,
            "title": rec["vacancy"].title,
            "description": rec["vacancy"].description,
            "grade": rec["vacancy"].grade,
            "score": rec["score"],
            "employer_name": rec["vacancy"].employer_name,
            "url": rec["vacancy"].url,
        }
        for rec in page_recommendations
    ]

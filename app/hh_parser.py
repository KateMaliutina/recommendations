import http

import requests
from sqlalchemy import select
from app.models import Vacancy, VacancySkill, Skill
from app.database import SessionLocal

# Настройки API
HH_API_URL = "https://api.hh.ru/vacancies"
HEADERS = {"User-Agent": "ProCareerParser/1.0"}


def fetch_vacancies(params):
    """ Запрос вакансий с API HH """
    response = requests.get(HH_API_URL, headers=HEADERS, params=params)
    if response.status_code == http.HTTPStatus.OK:
        return response.json().get("items", [])  # Возвращаем список вакансий
    return []


def fetch_vacancy_details(vacancy_id):
    """ Получение полной информации о вакансии по ID """
    url = f"{HH_API_URL}/{vacancy_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == http.HTTPStatus.OK:
        return response.json()
    return None


def save_vacancy(vacancy_data):
    db = SessionLocal()
    """ Сохранение вакансии в базу данных с полным описанием """
    try:
        vacancy_id = vacancy_data["id"]

        # Получаем полное описание вакансии
        full_vacancy = fetch_vacancy_details(vacancy_id)
        full_description = full_vacancy["description"] if full_vacancy else "Описание недоступно"

        vacancy = Vacancy(
            title=vacancy_data["name"],  # todo handle junior/младший + intern/стажировка/начинающий
            description=full_description,
            grade=vacancy_data.get("experience", {}).get("name", "Не указано"),
        )
        db.add(vacancy)
        db.commit()  # Фиксируем сохранение вакансии
        db.refresh(vacancy)  # Обновляем объект, чтобы получить ID

        # Сохраняем навыки
        skills = full_vacancy.get("key_skills", [])
        for skill_data in skills:
            skill_name = skill_data["name"].lower()

            # Проверяем, есть ли такой скилл в базе
            existing_skill = db.execute(select(Skill).where(Skill.name == skill_name)).scalar_one_or_none()
            if not existing_skill:
                existing_skill = Skill(name=skill_name)
                db.add(existing_skill)
                db.commit()  # Фиксируем добавление скилла
                db.refresh(existing_skill)

            # Добавляем связь с вакансией
            vacancy_skill = VacancySkill(vacancy_id=vacancy.id, skill_id=existing_skill.id)
            db.add(vacancy_skill)

        db.commit()  # Фиксируем добавление связей
    except Exception as e:
        db.rollback()  # Откатываем в случае ошибки
        print(f"Ошибка при сохранении вакансии: {e}")
    finally:
        db.close()  # Закрываем сессию в конце

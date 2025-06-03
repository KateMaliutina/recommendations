import http
import re
import requests
from sqlalchemy import select
from app.models import Vacancy, VacancySkill, Skill
from app.database import SessionLocal

# Настройки API
HH_API_URL = "https://api.hh.ru/vacancies"
HEADERS = {"User-Agent": "ProCareerParser/1.0"}

CLEANR = re.compile('<.*?>')


def cleanhtml(raw_html: str) -> str:
    cleantext = re.sub(CLEANR, '', raw_html)
    return cleantext


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
        hh_id = str(vacancy_data["id"])
        # Проверяем, есть ли такая вакансия в базе
        existing = db.execute(select(Vacancy).where(Vacancy.hh_id == hh_id)).scalar_one_or_none()
        if existing:
            print(f"Вакансия с hh_id={hh_id} уже существует — пропуск.")
            return  # Пропускаем сохранение
        vacancy_id = vacancy_data["id"]

        # Получаем полное описание вакансии
        full_vacancy = fetch_vacancy_details(hh_id)
        full_description = cleanhtml(full_vacancy["description"] if full_vacancy else "Описание недоступно").strip()

        vacancy = Vacancy(
            hh_id=hh_id,
            title=vacancy_data["name"],
            description=full_description,
            grade=fill_grade(vacancy_data["name"].lower()),
            employer_name=vacancy_data.get("employer", {}).get("name", "Не указано"),
            url=vacancy_data["alternate_url"],
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


def fill_grade(init_grade: str) -> str:
    grade = "Junior"

    if ("junior" in init_grade or
            "младший" in init_grade or
            "начинающий" in init_grade):
        grade = "Junior"
    elif ("intern" in init_grade or
          "стажер" in init_grade or
          "стажировка" in init_grade or
          "стажирующийся" in init_grade or
          "стажёр" in init_grade):
        grade = "Intern"
    elif ("middle" in init_grade or
          "специалист" in init_grade or
          "мидл" in init_grade or
          "средний" in init_grade):
        grade = "Middle"
    elif ("senior" in init_grade or
          "старший" in init_grade or
          "ведущий" in init_grade or
          "синьор" in init_grade or
          "сеньор" in init_grade):
        grade = "Senior"

    return grade

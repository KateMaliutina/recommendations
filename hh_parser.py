import requests
from sqlalchemy import select, create_engine
from sqlalchemy.orm import sessionmaker
from concurrent.futures import ProcessPoolExecutor, as_completed
from models import Vacancy, VacancySkill, Skill  # Подключаем модели

# ✅ Настройки API
HH_API_URL = "https://api.hh.ru/vacancies"
HEADERS = {"User-Agent": "ProCareerParser/1.0"}

# ✅ Настройки базы данных (СИНХРОННОЕ подключение!)
DATABASE_URL = "postgresql+psycopg2://postgres:postgres@localhost/recommendations"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)


def fetch_vacancies(params):
    """ Запрос вакансий с API HH """
    response = requests.get(HH_API_URL, headers=HEADERS, params=params)
    if response.status_code == 200:
        return response.json().get("items", [])  # Возвращаем список вакансий
    return []


def fetch_vacancy_details(vacancy_id):
    """ Получение полной информации о вакансии по ID """
    url = f"{HH_API_URL}/{vacancy_id}"
    response = requests.get(url, headers=HEADERS)
    if response.status_code == 200:
        return response.json()
    return None


def save_vacancy(vacancy_data):
    """ Сохранение вакансии в базу данных с полным описанием """
    db = SessionLocal()  # Открываем новую сессию
    try:
        vacancy_id = vacancy_data["id"]

        # Получаем полное описание вакансии
        full_vacancy = fetch_vacancy_details(vacancy_id)
        full_description = full_vacancy["description"] if full_vacancy else "Описание недоступно"

        vacancy = Vacancy(
            title=vacancy_data["name"],
            description=full_description,
            level=vacancy_data.get("experience", {}).get("name", "Не указано"),
        )
        db.add(vacancy)
        db.commit()  # Фиксируем сохранение вакансии
        db.refresh(vacancy)  # Обновляем объект, чтобы получить ID

        # ✅ Сохраняем навыки
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


def main():
    """ Основной процесс парсинга с многопоточностью """
    params = {
        "text": "Python разработчик",  # Фильтр по ключевому слову
        "area": 2,  # ID региона (Москва=1, СПб=2)
        "per_page": 20,  # Количество вакансий на страницу
    }

    vacancies = fetch_vacancies(params)

    # ✅ Используем ProcessPoolExecutor для ускорения
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(save_vacancy, vacancy): vacancy for vacancy in vacancies}

        for future in as_completed(futures):
            try:
                future.result()  # Вызываем, чтобы обработать возможные исключения
            except Exception as e:
                print(f"Ошибка при обработке вакансии: {e}")


if __name__ == "__main__":
    main()

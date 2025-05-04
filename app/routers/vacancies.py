import http

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.crud import create_vacancy, get_vacancies, get_one_vacancy
from pydantic import BaseModel

router = APIRouter()


# Pydantic-модель для валидации
class VacancyCreate(BaseModel):
    title: str
    description: str
    grade: str
    employer_name: str
    url: str


@router.post("/vacancies/")
async def add_vacancy(vacancy: VacancyCreate, db: AsyncSession = Depends(get_db)):
    """Создание вакансии"""
    return await create_vacancy(db,
                                vacancy.title,
                                vacancy.description,
                                vacancy.grade,
                                vacancy.employer_name,
                                vacancy.url)


@router.get("/vacancies/{vacancy_id}")
async def get_vacancy(vacancy_id: int, db: AsyncSession = Depends(get_db)):
    """Получение вакансии по id"""
    vacancy = await get_one_vacancy(db, vacancy_id)
    if not vacancy:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Вакансия не найдена")

    return vacancy


@router.get("/vacancies/")
async def list_vacancies(db: AsyncSession = Depends(get_db)):
    """Получение всех вакансий"""
    return await get_vacancies(db)

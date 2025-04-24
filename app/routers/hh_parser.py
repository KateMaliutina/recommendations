import http

from fastapi import APIRouter, HTTPException, Query, Depends
from concurrent.futures import ProcessPoolExecutor, as_completed
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import get_db
from app.hh_parser import fetch_vacancies, save_vacancy

router = APIRouter()


@router.post("/parse-hh-vacancies")
def parse_vacancies(
        text: str = Query(..., description="Ключевое слово для поиска вакансий"),
        area: int = Query(1, description="Регион поиска (Москва=1, СПб=2 и т.д.)"),
        per_page: int = Query(20, description="Количество вакансий на страницу"),
        db: AsyncSession = Depends(get_db)
):
    """Запускает парсинг вакансий по заданным параметрам"""
    params = {
        "text": text,
        "area": area,
        "per_page": per_page
    }
    vacancies = fetch_vacancies(params)

    # Используем ProcessPoolExecutor для ускорения
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(save_vacancy, vacancy, db): vacancy for vacancy in vacancies}

        e = HTTPException
        for future in as_completed(futures):
            try:
                future.result()  # Вызываем, чтобы обработать возможные исключения
            except Exception as e:
                print(f"Ошибка при обработке вакансии: {e}")
        if e is not None:  # todo test
            raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=e)

    return {"parsed": len(vacancies)}

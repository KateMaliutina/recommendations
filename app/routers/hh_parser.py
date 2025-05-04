import http

from fastapi import APIRouter, HTTPException, Query
from concurrent.futures import ProcessPoolExecutor, as_completed
from app.hh_parser import fetch_vacancies, save_vacancy

router = APIRouter()


@router.post("/parse-hh-vacancies")
def parse_vacancies(
        text: str = Query(..., description="Ключевые слова для поиска вакансий"),
        # area: int = Query(1, description="Регион поиска (Москва=1, СПб=2 и т.д.)"),
        per_page: int = Query(20, description="Количество вакансий на страницу")
):
    """Запускает парсинг вакансий по заданным параметрам"""
    params = [
        ("text", text),
        ("area", 1),  # Москва
        ("area", 2),  # Санкт-Петербург
        ("area", 3),  # Екатеринбург
        ("area", 4),  # Новосибирск
        ("per_page", per_page)
    ]
    vacancies = fetch_vacancies(params)

    # Используем ProcessPoolExecutor для ускорения
    with ProcessPoolExecutor(max_workers=5) as executor:
        futures = {executor.submit(save_vacancy, vacancy): vacancy for vacancy in vacancies}

        for future in as_completed(futures):
            try:
                future.result()  # Вызываем, чтобы обработать возможные исключения
            except Exception as e:
                print(f"Ошибка при обработке вакансии: {e}")
                raise HTTPException(status_code=http.HTTPStatus.INTERNAL_SERVER_ERROR, detail=e)

    return {"parsed": len(vacancies)}
# todo get request for getting areas

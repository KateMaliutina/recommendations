import http

from fastapi import APIRouter, HTTPException, Query
from concurrent.futures import ProcessPoolExecutor, as_completed

router = APIRouter()


@router.get("/")
def get_roadmap():
    pass

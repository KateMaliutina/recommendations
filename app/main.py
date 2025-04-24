from fastapi import FastAPI

from app.routers import users, skills, vacancies, hh_parser, recommendations

app = FastAPI()


app.include_router(recommendations.router, tags=["Recommendations"])
app.include_router(users.router, tags=["Users"])
app.include_router(skills.router, tags=["Skills"])
app.include_router(vacancies.router, tags=["Vacancies"])
app.include_router(hh_parser.router, tags=["Parser HH.ru"])


@app.get("/")
async def root():
    return {"message": "recommendation service works"}

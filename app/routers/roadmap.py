import http

import sqlalchemy
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from pydantic import BaseModel
from enum import Enum
from app.database import get_db
from app.models import User, Roadmap, RoadmapNode, UserRoadmapNode, SkillStatus

router = APIRouter()


@router.get("/users/{user_id}/roadmap")
async def get_user_roadmap(user_id: int, db: AsyncSession = Depends(get_db)):
    # 1. Найти пользователя
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Пользователь не найден")

    if user.specialization is None or user.specialization == "":
        raise HTTPException(status_code=http.HTTPStatus.CONFLICT, detail="У пользователя не заполнена специализация")

    specialization = user.specialization
    grade = "intern"

    # 2. Найти roadmap (сначала динамический, потом статический)
    roadmap_result = await db.execute(
        select(Roadmap).where(
            Roadmap.specialization == specialization,
            Roadmap.grade == grade
        ).order_by(Roadmap.is_dynamic.desc())
    )
    roadmap = roadmap_result.scalars().first()
    if not roadmap:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND,
                            detail="Роадмап не найден для данной специализации и грейда")

    # 3. Получить все roadmap_nodes (связанные с roadmap)
    nodes_result = await db.execute(
        select(RoadmapNode).where(RoadmapNode.roadmap_id == roadmap.id).options(
            # загружаем skill в одну выборку
            sqlalchemy.orm.selectinload(RoadmapNode.skill)
        )
    )
    nodes = nodes_result.scalars().all()

    user_nodes_result = await db.execute(
        select(UserRoadmapNode).where(UserRoadmapNode.user_id == user.id)
    )
    user_nodes = {node.roadmap_node_id: node.status for node in user_nodes_result.scalars().all()}

    roadmap_skills = []
    for node in nodes:
        status = user_nodes.get(node.id, SkillStatus.not_started)
        roadmap_skills.append({
            "node_id": node.id,
            "skill_id": node.skill.id,
            "parent_id": node.parent_id,
            "skill_name": node.skill.name,
            "status": status,
            "is_optional": node.is_optional
        })

    return {
        "specialization": specialization,
        "grade": grade,
        "skills": roadmap_skills
    }


class SkillStatusUpdate(str, Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    learned = "learned"


class UpdateNodeStatusRequest(BaseModel):
    node_id: int
    status: SkillStatusUpdate


@router.post("/users/{user_id}/roadmap/update-node-status")
async def update_node_status(user_id: int, update: UpdateNodeStatusRequest, db: AsyncSession = Depends(get_db)):
    # Проверим есть ли user
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Пользователь не найден")

    # Проверим node существует ли
    node_result = await db.execute(select(RoadmapNode).where(RoadmapNode.id == update.node_id))
    node = node_result.scalar_one_or_none()
    if not node:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Навык роадмапа не найден")

    # Проверим, есть ли запись в user_roadmap_nodes
    user_node_result = await db.execute(
        select(UserRoadmapNode).where(
            UserRoadmapNode.user_id == user.id,
            UserRoadmapNode.roadmap_node_id == node.id
        )
    )
    user_node = user_node_result.scalar_one_or_none()

    if user_node:
        user_node.status = update.status
    else:
        user_node = UserRoadmapNode(
            user_id=user.id,
            roadmap_node_id=node.id,
            status=update.status
        )
        db.add(user_node)

    await db.commit()
    return {"message": "Статус навыка обновлен", "node_id": node.id, "status": update.status}


@router.post("/users/{user_id}/generate-dynamic-roadmap")
async def generate_dynamic_roadmap(user_id: int, db: AsyncSession = Depends(get_db)):
    # 1. Проверим существует ли пользователь
    user_result = await db.execute(select(User).where(User.id == user_id))
    user = user_result.scalar_one_or_none()
    if not user:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Пользователь не найден")

    if not user.specialization:
        raise HTTPException(status_code=http.HTTPStatus.CONFLICT, detail="У пользователя не заполнена специализация")

    specialization = user.specialization
    grade = "intern"  # по умолчанию

    # 2. Соберем статистику навыков из вакансий по специализации
    # Предположим, что у вас есть таблица VacancySkill -> Vacancy -> specialization
    skills_count_result = await db.execute(
        sqlalchemy.text("""
            SELECT s.id, s.name, COUNT(*) as freq
            FROM skills s
            JOIN vacancy_skills vs ON s.id = vs.skill_id
            JOIN vacancies v ON v.id = vs.vacancy_id
            WHERE v.title ILIKE :title_pattern
            GROUP BY s.id, s.name
            ORDER BY freq DESC
        """),
        {"title_pattern": f"%{specialization}%"}
    )
    skill_rows = skills_count_result.fetchall()
    if not skill_rows:
        raise HTTPException(status_code=http.HTTPStatus.NOT_FOUND, detail="Нет данных по вакансиям для анализа")

    # 3. Найдем или создадим роадмап динамический
    roadmap_result = await db.execute(
        select(Roadmap).where(
            Roadmap.specialization == specialization,
            Roadmap.grade == grade,
            Roadmap.is_dynamic.is_(True)
        )
    )
    roadmap = roadmap_result.scalar_one_or_none()
    if not roadmap:
        roadmap = Roadmap(specialization=specialization, grade=grade, is_dynamic=True)
        db.add(roadmap)
        await db.commit()
        await db.refresh(roadmap)

    # 4. Создадим nodes (если их еще нет)
    created_nodes = []
    for skill_row in skill_rows:
        skill_id = skill_row[0]
        freq = skill_row[2]
        # Логика приоритета: например, is_optional = False если встречается >5 раз
        is_optional = freq < 5

        # Проверим, есть ли уже node для этого skill
        existing_node = await db.execute(
            select(RoadmapNode).where(
                RoadmapNode.roadmap_id == roadmap.id,
                RoadmapNode.skill_id == skill_id
            )
        )
        if not existing_node.scalar_one_or_none():
            node = RoadmapNode(
                roadmap_id=roadmap.id,
                skill_id=skill_id,
                is_optional=is_optional
            )
            db.add(node)
            created_nodes.append(skill_row[1])  # skill name

    await db.commit()

    return {"message": "Динамический роадмап сгенерирован", "skills_added": created_nodes}

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
        raise HTTPException(status_code=404, detail="User not found")

    if user.specialization is None or user.specialization == "":
        raise HTTPException(status_code=409, detail="User doesn't have specialization")
    if user.grade is None or user.grade == "": # todo hardcode junior
        raise HTTPException(status_code=409, detail="User doesn't have grade")
    specialization = user.specialization
    grade = user.grade

    # 2. Найти roadmap
    roadmap_result = await db.execute(
        select(Roadmap).where(
            Roadmap.specialization == specialization,
            Roadmap.grade == grade
        )
    )
    roadmap = roadmap_result.scalar_one_or_none()
    if not roadmap:
        raise HTTPException(status_code=404, detail="Roadmap not found for user specialization and grade")

    # 3. Получить все roadmap_nodes (связанные с roadmap)
    nodes_result = await db.execute(
        select(RoadmapNode).where(RoadmapNode.roadmap_id == roadmap.id).options(
            # загружаем skill в одну выборку
            sqlalchemy.orm.selectinload(RoadmapNode.skill)  # todo test
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
            "skill_name": node.skill.name,
            "status": status
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
        raise HTTPException(status_code=404, detail="User not found")

    # Проверим node существует ли
    node_result = await db.execute(select(RoadmapNode).where(RoadmapNode.id == update.node_id))
    node = node_result.scalar_one_or_none()
    if not node:
        raise HTTPException(status_code=404, detail="Roadmap node not found")

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
    return {"message": "Status updated", "node_id": node.id, "status": update.status}

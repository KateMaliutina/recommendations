from sqlalchemy import Column, Integer, String, ForeignKey, ARRAY, Boolean, UniqueConstraint, Enum
from sqlalchemy.orm import declarative_base, relationship
import enum

Base = declarative_base()


# Таблица навыков
class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    grade = Column(String, nullable=True)  # junior/middle/senior
    interests = Column(ARRAY(String), nullable=True)
    specialization = Column(String, nullable=True)

    skills = relationship("UserSkill", back_populates="user")


# Связь пользователей и навыков
class UserSkill(Base):
    __tablename__ = "user_skills"

    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)
    proficiency_level = Column(Integer, nullable=False)  # 0-100

    user = relationship("User", back_populates="skills")
    skill = relationship("Skill")


# Таблица вакансий
class Vacancy(Base):
    __tablename__ = "vacancies"

    id = Column(Integer, primary_key=True, index=True)
    hh_id = Column(String, unique=True, nullable=False)  # Внешний ID от HeadHunter
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    grade = Column(String, nullable=False)
    employer_name = Column(String, nullable=False)
    url = Column(String, nullable=False)

    skills = relationship("VacancySkill", back_populates="vacancy")


# Связь вакансий и навыков
class VacancySkill(Base):
    __tablename__ = "vacancy_skills"

    vacancy_id = Column(Integer, ForeignKey("vacancies.id"), primary_key=True)
    skill_id = Column(Integer, ForeignKey("skills.id"), primary_key=True)

    vacancy = relationship("Vacancy", back_populates="skills")
    skill = relationship("Skill")


# Таблица рекомендаций
class Recommendation(Base):
    __tablename__ = "recommendations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    vacancy_id = Column(Integer, ForeignKey("vacancies.id"))
    score = Column(Integer, nullable=False)  # 1-100


# таблица роудмапов
class Roadmap(Base):
    __tablename__ = "roadmaps"
    id = Column(Integer, primary_key=True, index=True)
    specialization = Column(String, nullable=False)  # например frontend, backend
    grade = Column(String, nullable=False)  # intern, junior...
    is_dynamic = Column(Boolean, default=False, nullable=True)  # Новый признак автогенерируемости
    __table_args__ = (
        UniqueConstraint('specialization', 'grade', 'is_dynamic', name='_specialization_grade_dynamic_uc'),
    )

    nodes = relationship("RoadmapNode", back_populates="roadmap")


# таблица скиллов для роудмапа
class RoadmapNode(Base):
    __tablename__ = "roadmap_nodes"
    id = Column(Integer, primary_key=True, index=True)
    roadmap_id = Column(Integer, ForeignKey("roadmaps.id"), nullable=False)
    skill_id = Column(Integer, ForeignKey("skills.id"), nullable=False)
    parent_id = Column(Integer, ForeignKey("roadmap_nodes.id"), nullable=True)
    is_optional = Column(Boolean, default=False)

    roadmap = relationship("Roadmap", back_populates="nodes")
    skill = relationship("Skill")
    children = relationship("RoadmapNode", backref="parent", remote_side=[id])


class SkillStatus(str, enum.Enum):
    not_started = "not_started"
    in_progress = "in_progress"
    learned = "learned"


class UserRoadmapNode(Base):
    __tablename__ = "user_roadmap_nodes"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    roadmap_node_id = Column(Integer, ForeignKey("roadmap_nodes.id"), nullable=False)
    status = Column(Enum(SkillStatus), default=SkillStatus.not_started, nullable=False)

    __table_args__ = (UniqueConstraint('user_id', 'roadmap_node_id', name='_user_node_uc'),)

    user = relationship("User", back_populates="user_roadmap_nodes")
    roadmap_node = relationship("RoadmapNode", back_populates="user_roadmap_nodes")


# Добавляем обратные связи:
User.user_roadmap_nodes = relationship("UserRoadmapNode", back_populates="user", cascade="all, delete-orphan")
RoadmapNode.user_roadmap_nodes = relationship("UserRoadmapNode", back_populates="roadmap_node",
                                              cascade="all, delete-orphan")

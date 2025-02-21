from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


# Таблица навыков
class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)


# Таблица пользователей
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    level = Column(String, nullable=False)  # junior/middle/senior
    interests = Column(String, nullable=True)

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
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    level = Column(String, nullable=False)

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

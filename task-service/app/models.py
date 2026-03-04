from sqlalchemy import Column, Integer, String
from app.db import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(255))
    description = Column(String(255))
    owner_id = Column(Integer)

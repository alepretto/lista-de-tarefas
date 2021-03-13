from datetime import datetime

from config.database import Base

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, TIMESTAMP, Boolean


class Tarefa(Base):
    __tablename__ = "tarefas"

    id_tarefa = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String)
    descricao = Column(String)
    concluido = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP, default=datetime.now())
    updated_at = Column(TIMESTAMP, default=datetime.now(), onupdate=datetime.now())
    deleted_at = Column(TIMESTAMP)

from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class CreateTarefa(BaseModel):
    nome: str
    descricao: str


class TarefaSchema(CreateTarefa):
    id_tarefa: int
    concluido: bool
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class UpdateTarfea(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
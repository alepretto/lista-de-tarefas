from typing import List
from datetime import datetime

from ..schema.tarefa import CreateTarefa, TarefaSchema, UpdateTarfea
from ..models.Tarefa import Tarefa

from sqlalchemy.orm import Session


class TarefaService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create_tarefa(self, tarefa: CreateTarefa) -> TarefaSchema:
        nova_tarefa = Tarefa(**tarefa.dict())
        self.db.add(nova_tarefa)
        self.db.commit()
        self.db.refresh(nova_tarefa)

        return nova_tarefa

    def get_tarefas(self) -> List[TarefaSchema]:
        tarefas = self.db.query(Tarefa).filter(Tarefa.deleted_at == None).order_by(Tarefa.created_at.desc()).all()
        return tarefas

    def update_tarefa(self, id_tarefa: int, infos_tarefa: UpdateTarfea) -> TarefaSchema:
        infos_tarefa = infos_tarefa.dict(exclude_none=True)
        self.db.query(Tarefa).filter(Tarefa.id_tarefa == id_tarefa).update(infos_tarefa)
        self.db.commit()

        nova_tarefa = (
            self.db.query(Tarefa).filter(Tarefa.id_tarefa == id_tarefa).first()
        )
        return nova_tarefa

    def delete_tarefa(self, id_tarefa: int):
        self.db.query(Tarefa).filter(Tarefa.id_tarefa == id_tarefa).update(
            {"deleted_at": datetime.now()}
        )
        self.db.commit()

    def finalizar_tarefa(self, id_tarefa: int):
        self.db.query(Tarefa).filter(Tarefa.id_tarefa == id_tarefa).update(
            {"concluido": True}
        )
        self.db.commit()
        nova_tarefa = (
            self.db.query(Tarefa).filter(Tarefa.id_tarefa == id_tarefa).first()
        )
        return nova_tarefa

    def abrir_tarefa(self, id_tarefa: int):
        self.db.query(Tarefa).filter(Tarefa.id_tarefa == id_tarefa).update(
            {"concluido": False}
        )
        self.db.commit()
        nova_tarefa = (
            self.db.query(Tarefa).filter(Tarefa.id_tarefa == id_tarefa).first()
        )
        return nova_tarefa

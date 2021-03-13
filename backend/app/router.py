from typing import List
from config.database import get_db
from .schema.tarefa import CreateTarefa, TarefaSchema, UpdateTarfea
from .services.tarefa_services import TarefaService

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


router = APIRouter(prefix="/tarefas", tags=["tarefas"])


@router.post("/")
async def create_tarefa(
    tarefa: CreateTarefa, db: Session = Depends(get_db)
) -> TarefaSchema:
    tarefa_service = TarefaService(db)
    tarefa_criada = tarefa_service.create_tarefa(tarefa)
    return tarefa_criada


@router.get("/")
async def get_tarefas(db: Session = Depends(get_db)) -> List[TarefaSchema]:
    tarefa_service = TarefaService(db)
    return tarefa_service.get_tarefas()


@router.put("/{id_tarefa}")
async def update_tarefa(
    id_tarefa: int, infos_tarefas: UpdateTarfea, db: Session = Depends(get_db)
):
    tarefa_service = TarefaService(db)
    tarefa_atualizada = tarefa_service.update_tarefa(id_tarefa, infos_tarefas)
    return tarefa_atualizada


@router.delete("/{id_tarefa}")
async def delete_tarefa(id_tarefa: int, db: Session = Depends(get_db)):
    tarefa_saervice = TarefaService(db)
    tarefa_saervice.delete_tarefa(id_tarefa)

    return {"msg": "Registro Excluído com sucesso"}


@router.patch("/{id_tarefa}/concluir")
async def conclui_tarefa(id_tarefa: int, db: Session = Depends(get_db)):
    tarefa_saervice = TarefaService(db)
    tarefa = tarefa_saervice.finalizar_tarefa(id_tarefa)

    return {"msg": tarefa}


@router.patch("/{id_tarefa}/abrir")
async def abri_tarefa(id_tarefa: int, db: Session = Depends(get_db)):
    tarefa_saervice = TarefaService(db)
    tarefa = tarefa_saervice.abrir_tarefa(id_tarefa)

    return {"msg": tarefa}

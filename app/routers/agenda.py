from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/agenda", tags=["agenda"])


@router.post("/", response_model=schemas.AgendaRead)
def create_agenda(agenda: schemas.AgendaCreate, db: Session = Depends(get_db)):
    """Cria um novo registro na agenda."""
    return crud.create_agenda(db, agenda)


@router.get("/", response_model=List[schemas.AgendaRead])
def list_agenda(db: Session = Depends(get_db)):
    """Retorna todas as entradas da agenda."""
    return crud.get_agendas(db)


@router.get("/{agenda_id}", response_model=schemas.AgendaRead)
def get_agenda(agenda_id: int, db: Session = Depends(get_db)):
    db_agenda = crud.get_agenda(db, agenda_id)
    if not db_agenda:
        raise HTTPException(status_code=404, detail="Entrada de agenda não encontrada")
    return db_agenda


@router.put("/{agenda_id}", response_model=schemas.AgendaRead)
def update_agenda(agenda_id: int, agenda: schemas.AgendaCreate, db: Session = Depends(get_db)):
    db_agenda = crud.update_agenda(db, agenda_id, agenda)
    if not db_agenda:
        raise HTTPException(status_code=404, detail="Entrada de agenda não encontrada")
    return db_agenda


@router.patch("/{agenda_id}", response_model=schemas.AgendaRead)
def patch_agenda(agenda_id: int, agenda: schemas.AgendaUpdate, db: Session = Depends(get_db)):
    """
    Atualiza parcialmente uma entrada da agenda.

    Campos não enviados não serão alterados.
    """
    data = agenda.dict(exclude_unset=True)
    if not data:
        return crud.get_agenda(db, agenda_id)
    db_agenda = crud.patch_agenda(db, agenda_id, data)
    if not db_agenda:
        raise HTTPException(status_code=404, detail="Entrada de agenda não encontrada")
    return db_agenda


@router.delete("/{agenda_id}")
def delete_agenda(agenda_id: int, db: Session = Depends(get_db)):
    success = crud.delete_agenda(db, agenda_id)
    if not success:
        raise HTTPException(status_code=404, detail="Entrada de agenda não encontrada")
    return {"detail": "Entrada de agenda deletada"}

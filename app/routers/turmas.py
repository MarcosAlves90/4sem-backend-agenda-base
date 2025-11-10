from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/turmas", tags=["turmas"])


@router.post("/", response_model=schemas.TurmaRead)
def create_turma(turma: schemas.TurmaCreate, db: Session = Depends(get_db)):
    """Cria uma nova turma no banco de dados."""
    return crud.create_turma(db, turma)


@router.get("/", response_model=List[schemas.TurmaRead])
def list_turmas(db: Session = Depends(get_db)):
    """Retorna todas as turmas."""
    return crud.get_turmas(db)


@router.get("/{turma_id}", response_model=schemas.TurmaRead)
def get_turma(turma_id: int, db: Session = Depends(get_db)):
    db_turma = crud.get_turma(db, turma_id)
    if not db_turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return db_turma


@router.put("/{turma_id}", response_model=schemas.TurmaRead)
def update_turma(turma_id: int, turma: schemas.TurmaCreate, db: Session = Depends(get_db)):
    db_turma = crud.update_turma(db, turma_id, turma)
    if not db_turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return db_turma


@router.patch("/{turma_id}", response_model=schemas.TurmaRead)
def patch_turma(turma_id: int, turma: schemas.TurmaUpdate, db: Session = Depends(get_db)):
    """
    Atualiza parcialmente os dados de uma turma.

    Campos não enviados não serão alterados.
    """
    data = turma.dict(exclude_unset=True)
    if not data:
        return crud.get_turma(db, turma_id)
    db_turma = crud.patch_turma(db, turma_id, data)
    if not db_turma:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return db_turma


@router.delete("/{turma_id}")
def delete_turma(turma_id: int, db: Session = Depends(get_db)):
    success = crud.delete_turma(db, turma_id)
    if not success:
        raise HTTPException(status_code=404, detail="Turma não encontrada")
    return {"detail": "Turma deletada"}

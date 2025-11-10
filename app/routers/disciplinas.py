from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/disciplinas", tags=["disciplinas"])


@router.post("/", response_model=schemas.DisciplinaRead)
def create_disciplina(disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    """Cria uma nova disciplina."""
    return crud.create_disciplina(db, disciplina)


@router.get("/", response_model=List[schemas.DisciplinaRead])
def list_disciplinas(db: Session = Depends(get_db)):
    """Retorna todas as disciplinas."""
    return crud.get_disciplinas(db)


@router.get("/{disciplina_id}", response_model=schemas.DisciplinaRead)
def get_disciplina(disciplina_id: int, db: Session = Depends(get_db)):
    db_disc = crud.get_disciplina(db, disciplina_id)
    if not db_disc:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return db_disc


@router.put("/{disciplina_id}", response_model=schemas.DisciplinaRead)
def update_disciplina(disciplina_id: int, disciplina: schemas.DisciplinaCreate, db: Session = Depends(get_db)):
    db_disc = crud.update_disciplina(db, disciplina_id, disciplina)
    if not db_disc:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return db_disc


@router.patch("/{disciplina_id}", response_model=schemas.DisciplinaRead)
def patch_disciplina(disciplina_id: int, disciplina: schemas.DisciplinaUpdate, db: Session = Depends(get_db)):
    """
    Atualiza parcialmente os dados de uma disciplina.

    Campos não enviados não serão alterados.
    """
    data = disciplina.dict(exclude_unset=True)
    if not data:
        return crud.get_disciplina(db, disciplina_id)
    db_disc = crud.patch_disciplina(db, disciplina_id, data)
    if not db_disc:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return db_disc


@router.delete("/{disciplina_id}")
def delete_disciplina(disciplina_id: int, db: Session = Depends(get_db)):
    success = crud.delete_disciplina(db, disciplina_id)
    if not success:
        raise HTTPException(status_code=404, detail="Disciplina não encontrada")
    return {"detail": "Disciplina deletada"}

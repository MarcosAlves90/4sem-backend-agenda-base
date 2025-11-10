from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/professores", tags=["professores"])


@router.post("/", response_model=schemas.ProfessorRead)
def create_professor(professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    """Cria um novo professor no banco de dados."""
    existing = db.query(models.Professor).filter(models.Professor.email == professor.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_professor(db, professor)


@router.get("/", response_model=List[schemas.ProfessorRead])
def list_professores(db: Session = Depends(get_db)):
    """Retorna todos os professores."""
    return crud.get_professores(db)


@router.get("/{professor_id}", response_model=schemas.ProfessorRead)
def get_professor(professor_id: int, db: Session = Depends(get_db)):
    db_prof = crud.get_professor(db, professor_id)
    if not db_prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return db_prof


@router.put("/{professor_id}", response_model=schemas.ProfessorRead)
def update_professor(professor_id: int, professor: schemas.ProfessorCreate, db: Session = Depends(get_db)):
    db_prof = crud.update_professor(db, professor_id, professor)
    if not db_prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return db_prof


@router.patch("/{professor_id}", response_model=schemas.ProfessorRead)
def patch_professor(professor_id: int, professor: schemas.ProfessorUpdate, db: Session = Depends(get_db)):
    """
    Atualiza parcialmente os dados de um professor.

    Campos não enviados não serão alterados.
    """
    data = professor.dict(exclude_unset=True)
    if not data:
        return crud.get_professor(db, professor_id)
    db_prof = crud.patch_professor(db, professor_id, data)
    if not db_prof:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return db_prof


@router.delete("/{professor_id}")
def delete_professor(professor_id: int, db: Session = Depends(get_db)):
    success = crud.delete_professor(db, professor_id)
    if not success:
        raise HTTPException(status_code=404, detail="Professor não encontrado")
    return {"detail": "Professor deletado"}

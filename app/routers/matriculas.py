from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/matriculas", tags=["matriculas"])


@router.post("/", response_model=schemas.MatriculaRead)
def create_matricula(matricula: schemas.MatriculaCreate, db: Session = Depends(get_db)):
    """Cria uma nova matrícula ligando um aluno a uma turma."""
    aluno = crud.get_aluno(db, matricula.aluno_id)
    turma = crud.get_turma(db, matricula.turma_id)
    if not aluno or not turma:
        raise HTTPException(status_code=400, detail="Aluno ou Turma inválidos")
    return crud.create_matricula(db, matricula)


@router.get("/", response_model=List[schemas.MatriculaRead])
def list_matriculas(db: Session = Depends(get_db)):
    """Retorna todas as matrículas."""
    return crud.get_matriculas(db)


@router.get("/{matricula_id}", response_model=schemas.MatriculaRead)
def get_matricula(matricula_id: int, db: Session = Depends(get_db)):
    db_m = crud.get_matricula(db, matricula_id)
    if not db_m:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")
    return db_m


@router.patch("/{matricula_id}", response_model=schemas.MatriculaRead)
def patch_matricula(matricula_id: int, matricula: schemas.MatriculaUpdate, db: Session = Depends(get_db)):
    """
    Atualiza parcialmente os dados de uma matrícula (aluno_id e/ou turma_id).

    Campos não enviados não serão alterados.
    """
    data = matricula.dict(exclude_unset=True)
    if not data:
        return crud.get_matricula(db, matricula_id)
    # opcional: validar se novo aluno/turma existem
    if "aluno_id" in data and not crud.get_aluno(db, data["aluno_id"]):
        raise HTTPException(status_code=400, detail="Aluno inválido")
    if "turma_id" in data and not crud.get_turma(db, data["turma_id"]):
        raise HTTPException(status_code=400, detail="Turma inválida")
    db_m = crud.patch_matricula(db, matricula_id, data)
    if not db_m:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")
    return db_m


@router.delete("/{matricula_id}")
def delete_matricula(matricula_id: int, db: Session = Depends(get_db)):
    success = crud.delete_matricula(db, matricula_id)
    if not success:
        raise HTTPException(status_code=404, detail="Matrícula não encontrada")
    return {"detail": "Matrícula deletada"}

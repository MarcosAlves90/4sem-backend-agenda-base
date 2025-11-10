from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import models, schemas, crud
from ..database import get_db

router = APIRouter(prefix="/alunos", tags=["alunos"])


@router.post("/", response_model=schemas.AlunoRead)
def create_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    """
    Cria um novo aluno no banco de dados.

    - **aluno**: Dados do aluno a ser criado (nome, email, data_nascimento opcional).
    - **db**: Sessão do banco de dados (injetada automaticamente).

    Retorna o aluno criado com ID gerado.

    Levanta HTTPException 400 se o email já estiver cadastrado.
    """
    existing = db.query(models.Aluno).filter(models.Aluno.email == aluno.email).first()
    if existing:
        raise HTTPException(status_code=400, detail="Email já cadastrado")
    return crud.create_aluno(db, aluno)


@router.get("/", response_model=List[schemas.AlunoRead])
def list_alunos(db: Session = Depends(get_db)):
    """
    Retorna a lista de todos os alunos cadastrados.
    """
    return crud.get_alunos(db)


@router.get("/{aluno_id}", response_model=schemas.AlunoRead)
def get_aluno(aluno_id: int, db: Session = Depends(get_db)):
    """Retorna um aluno por ID."""
    db_aluno = crud.get_aluno(db, aluno_id)
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno


@router.put("/{aluno_id}", response_model=schemas.AlunoRead)
def update_aluno(aluno_id: int, aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    """Atualiza os dados de um aluno existente."""
    db_aluno = crud.update_aluno(db, aluno_id, aluno)
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno


@router.patch("/{aluno_id}", response_model=schemas.AlunoRead)
def patch_aluno(aluno_id: int, aluno: schemas.AlunoUpdate, db: Session = Depends(get_db)):
    """
    Atualiza parcialmente os dados de um aluno.

    Campos não enviados não serão alterados.
    """
    data = aluno.dict(exclude_unset=True)
    if not data:
        return crud.get_aluno(db, aluno_id)
    db_aluno = crud.patch_aluno(db, aluno_id, data)
    if not db_aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return db_aluno


@router.delete("/{aluno_id}")
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    """Remove um aluno por ID."""
    success = crud.delete_aluno(db, aluno_id)
    if not success:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {"detail": "Aluno deletado"}

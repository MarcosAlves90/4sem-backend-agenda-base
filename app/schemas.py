from typing import Optional, List
from datetime import date, time

from pydantic import BaseModel, EmailStr


class AlunoBase(BaseModel):
    nome: str
    email: EmailStr
    data_nascimento: Optional[date] = None


class AlunoCreate(AlunoBase):
    pass


class AlunoRead(AlunoBase):
    id: int

    class Config:
        from_attributes = True


class AlunoUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None
    data_nascimento: Optional[date] = None

    class Config:
        from_attributes = True


class AgendaBase(BaseModel):
    data: date
    hora_inicio: time
    hora_fim: time
    descricao: Optional[str] = None
    turma_id: Optional[int] = None
    disciplina_id: Optional[int] = None
    professor_id: Optional[int] = None


class AgendaCreate(AgendaBase):
    pass


class AgendaRead(AgendaBase):
    id: int

    class Config:
        from_attributes = True


class AgendaUpdate(BaseModel):
    data: Optional[date] = None
    hora_inicio: Optional[time] = None
    hora_fim: Optional[time] = None
    descricao: Optional[str] = None
    turma_id: Optional[int] = None
    disciplina_id: Optional[int] = None
    professor_id: Optional[int] = None

    class Config:
        from_attributes = True


class ProfessorBase(BaseModel):
    nome: str
    email: EmailStr


class ProfessorCreate(ProfessorBase):
    pass


class ProfessorRead(ProfessorBase):
    id: int

    class Config:
        from_attributes = True


class ProfessorUpdate(BaseModel):
    nome: Optional[str] = None
    email: Optional[EmailStr] = None

    class Config:
        from_attributes = True


class TurmaBase(BaseModel):
    nome: str
    ano: int


class TurmaCreate(TurmaBase):
    pass


class TurmaRead(TurmaBase):
    id: int

    class Config:
        from_attributes = True


class TurmaUpdate(BaseModel):
    nome: Optional[str] = None
    ano: Optional[int] = None

    class Config:
        from_attributes = True


class DisciplinaBase(BaseModel):
    nome: str


class DisciplinaCreate(DisciplinaBase):
    pass


class DisciplinaRead(DisciplinaBase):
    id: int

    class Config:
        from_attributes = True


class DisciplinaUpdate(BaseModel):
    nome: Optional[str] = None

    class Config:
        from_attributes = True


class MatriculaBase(BaseModel):
    aluno_id: int
    turma_id: int


class MatriculaCreate(MatriculaBase):
    pass


class MatriculaRead(MatriculaBase):
    id: int

    class Config:
        from_attributes = True


class MatriculaUpdate(BaseModel):
    aluno_id: Optional[int] = None
    turma_id: Optional[int] = None

    class Config:
        from_attributes = True

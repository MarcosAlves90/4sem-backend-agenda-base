from sqlalchemy import Column, Integer, String, Date, Time, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Aluno(Base):
    __tablename__ = "alunos"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    data_nascimento = Column(Date)


class Professor(Base):
    __tablename__ = "professores"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)


class Turma(Base):
    __tablename__ = "turmas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(50), nullable=False)
    ano = Column(Integer, nullable=False)


class Disciplina(Base):
    __tablename__ = "disciplinas"
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(100), nullable=False)


class Agenda(Base):
    __tablename__ = "agenda"
    id = Column(Integer, primary_key=True, index=True)
    data = Column(Date, nullable=False)
    hora_inicio = Column(Time, nullable=False)
    hora_fim = Column(Time, nullable=False)
    descricao = Column(String(255))
    turma_id = Column(Integer, ForeignKey("turmas.id"))
    disciplina_id = Column(Integer, ForeignKey("disciplinas.id"))
    professor_id = Column(Integer, ForeignKey("professores.id"))

    turma = relationship("Turma")
    disciplina = relationship("Disciplina")
    professor = relationship("Professor")


class Matricula(Base):
    __tablename__ = "matriculas"
    id = Column(Integer, primary_key=True, index=True)
    aluno_id = Column(Integer, ForeignKey("alunos.id"))
    turma_id = Column(Integer, ForeignKey("turmas.id"))

    aluno = relationship("Aluno")
    turma = relationship("Turma")

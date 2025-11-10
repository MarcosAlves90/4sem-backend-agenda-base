from sqlalchemy.orm import Session
from . import models, schemas


def get_alunos(db: Session):
    return db.query(models.Aluno).all()


def get_aluno(db: Session, aluno_id: int):
    return db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()


def create_aluno(db: Session, aluno: schemas.AlunoCreate):
    db_aluno = models.Aluno(**aluno.model_dump())
    db.add(db_aluno)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno


def get_agendas(db: Session):
    return db.query(models.Agenda).all()


def create_agenda(db: Session, agenda: schemas.AgendaCreate):
    db_agenda = models.Agenda(**agenda.model_dump())
    db.add(db_agenda)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda


def get_agenda(db: Session, agenda_id: int):
    return db.query(models.Agenda).filter(models.Agenda.id == agenda_id).first()


def update_aluno(db: Session, aluno_id: int, aluno: schemas.AlunoCreate):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        return None
    for key, value in aluno.model_dump().items():
        setattr(db_aluno, key, value)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno


def delete_aluno(db: Session, aluno_id: int):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        return False
    db.delete(db_aluno)
    db.commit()
    return True


def update_agenda(db: Session, agenda_id: int, agenda: schemas.AgendaCreate):
    db_agenda = db.query(models.Agenda).filter(models.Agenda.id == agenda_id).first()
    if not db_agenda:
        return None
    for key, value in agenda.model_dump().items():
        setattr(db_agenda, key, value)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda


def delete_agenda(db: Session, agenda_id: int):
    db_agenda = db.query(models.Agenda).filter(models.Agenda.id == agenda_id).first()
    if not db_agenda:
        return False
    db.delete(db_agenda)
    db.commit()
    return True


def patch_aluno(db: Session, aluno_id: int, data: dict):
    db_aluno = db.query(models.Aluno).filter(models.Aluno.id == aluno_id).first()
    if not db_aluno:
        return None
    for key, value in data.items():
        setattr(db_aluno, key, value)
    db.commit()
    db.refresh(db_aluno)
    return db_aluno


def patch_agenda(db: Session, agenda_id: int, data: dict):
    db_agenda = db.query(models.Agenda).filter(models.Agenda.id == agenda_id).first()
    if not db_agenda:
        return None
    for key, value in data.items():
        setattr(db_agenda, key, value)
    db.commit()
    db.refresh(db_agenda)
    return db_agenda


def patch_professor(db: Session, professor_id: int, data: dict):
    db_prof = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    if not db_prof:
        return None
    for key, value in data.items():
        setattr(db_prof, key, value)
    db.commit()
    db.refresh(db_prof)
    return db_prof


def patch_turma(db: Session, turma_id: int, data: dict):
    db_turma = db.query(models.Turma).filter(models.Turma.id == turma_id).first()
    if not db_turma:
        return None
    for key, value in data.items():
        setattr(db_turma, key, value)
    db.commit()
    db.refresh(db_turma)
    return db_turma


def patch_disciplina(db: Session, disciplina_id: int, data: dict):
    db_disc = db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id).first()
    if not db_disc:
        return None
    for key, value in data.items():
        setattr(db_disc, key, value)
    db.commit()
    db.refresh(db_disc)
    return db_disc


def patch_matricula(db: Session, matricula_id: int, data: dict):
    db_m = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not db_m:
        return None
    for key, value in data.items():
        setattr(db_m, key, value)
    db.commit()
    db.refresh(db_m)
    return db_m


def get_professores(db: Session):
    return db.query(models.Professor).all()


def get_professor(db: Session, professor_id: int):
    return db.query(models.Professor).filter(models.Professor.id == professor_id).first()


def create_professor(db: Session, professor: schemas.ProfessorCreate):
    db_prof = models.Professor(**professor.model_dump())
    db.add(db_prof)
    db.commit()
    db.refresh(db_prof)
    return db_prof


def update_professor(db: Session, professor_id: int, professor: schemas.ProfessorCreate):
    db_prof = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    if not db_prof:
        return None
    for key, value in professor.model_dump().items():
        setattr(db_prof, key, value)
    db.commit()
    db.refresh(db_prof)
    return db_prof


def delete_professor(db: Session, professor_id: int):
    db_prof = db.query(models.Professor).filter(models.Professor.id == professor_id).first()
    if not db_prof:
        return False
    db.delete(db_prof)
    db.commit()
    return True


def get_turmas(db: Session):
    return db.query(models.Turma).all()


def get_turma(db: Session, turma_id: int):
    return db.query(models.Turma).filter(models.Turma.id == turma_id).first()


def create_turma(db: Session, turma: schemas.TurmaCreate):
    db_turma = models.Turma(**turma.model_dump())
    db.add(db_turma)
    db.commit()
    db.refresh(db_turma)
    return db_turma


def update_turma(db: Session, turma_id: int, turma: schemas.TurmaCreate):
    db_turma = db.query(models.Turma).filter(models.Turma.id == turma_id).first()
    if not db_turma:
        return None
    for key, value in turma.model_dump().items():
        setattr(db_turma, key, value)
    db.commit()
    db.refresh(db_turma)
    return db_turma


def delete_turma(db: Session, turma_id: int):
    db_turma = db.query(models.Turma).filter(models.Turma.id == turma_id).first()
    if not db_turma:
        return False
    db.delete(db_turma)
    db.commit()
    return True


def get_disciplinas(db: Session):
    return db.query(models.Disciplina).all()


def get_disciplina(db: Session, disciplina_id: int):
    return db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id).first()


def create_disciplina(db: Session, disciplina: schemas.DisciplinaCreate):
    db_disc = models.Disciplina(**disciplina.model_dump())
    db.add(db_disc)
    db.commit()
    db.refresh(db_disc)
    return db_disc


def update_disciplina(db: Session, disciplina_id: int, disciplina: schemas.DisciplinaCreate):
    db_disc = db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id).first()
    if not db_disc:
        return None
    for key, value in disciplina.model_dump().items():
        setattr(db_disc, key, value)
    db.commit()
    db.refresh(db_disc)
    return db_disc


def delete_disciplina(db: Session, disciplina_id: int):
    db_disc = db.query(models.Disciplina).filter(models.Disciplina.id == disciplina_id).first()
    if not db_disc:
        return False
    db.delete(db_disc)
    db.commit()
    return True


def get_matriculas(db: Session):
    return db.query(models.Matricula).all()


def get_matricula(db: Session, matricula_id: int):
    return db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()


def create_matricula(db: Session, matricula: schemas.MatriculaCreate):
    # opcional: checar existência de aluno e turma
    db_m = models.Matricula(**matricula.model_dump())
    db.add(db_m)
    db.commit()
    db.refresh(db_m)
    return db_m


def delete_matricula(db: Session, matricula_id: int):
    db_m = db.query(models.Matricula).filter(models.Matricula.id == matricula_id).first()
    if not db_m:
        return False
    db.delete(db_m)
    db.commit()
    return True

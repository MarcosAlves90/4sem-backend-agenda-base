CREATE TABLE alunos (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    data_nascimento DATE
);

CREATE TABLE professores (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

CREATE TABLE turmas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(50) NOT NULL,
    ano INT NOT NULL
);

CREATE TABLE disciplinas (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

CREATE TABLE agenda (
    id SERIAL PRIMARY KEY,
    data DATE NOT NULL,
    hora_inicio TIME NOT NULL,
    hora_fim TIME NOT NULL,
    descricao VARCHAR(255),
    turma_id INT,
    disciplina_id INT,
    professor_id INT,
    FOREIGN KEY (turma_id) REFERENCES turmas(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id),
    FOREIGN KEY (professor_id) REFERENCES professores(id)
);

CREATE TABLE matriculas (
    id SERIAL PRIMARY KEY,
    aluno_id INT,
    turma_id INT,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (turma_id) REFERENCES turmas(id)
);


INSERT INTO alunos (nome, email, data_nascimento) VALUES
('Ana Silva', 'ana.silva@email.com', '2008-03-15'),
('Bruno Souza', 'bruno.souza@email.com', '2007-07-22'),
('Carla Mendes', 'carla.mendes@email.com', '2008-11-05');

INSERT INTO professores (nome, email) VALUES
('Prof. João Lima', 'joao.lima@escola.com'),
('Profª. Maria Rosa', 'maria.rosa@escola.com');

INSERT INTO turmas (nome, ano) VALUES
('6º Ano A', 2024),
('7º Ano B', 2024);

INSERT INTO disciplinas (nome) VALUES
('Matemática'),
('Português');

INSERT INTO agenda (data, hora_inicio, hora_fim, descricao, turma_id, disciplina_id, professor_id) VALUES
('2024-11-10', '08:00', '09:40', 'Aula de Matemática', 1, 1, 1),
('2024-11-10', '10:00', '11:40', 'Aula de Português', 2, 2, 2);

INSERT INTO matriculas (aluno_id, turma_id) VALUES
(1, 1),
(2, 1),
(3, 2);
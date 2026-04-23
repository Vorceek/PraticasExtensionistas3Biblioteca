CREATE TABLE Usuario (
    id_usuario INT PRIMARY KEY,
    nome VARCHAR(100),
    cpf VARCHAR(20),
    email VARCHAR(100)
);

CREATE TABLE Funcionario (
    id_funcionario INT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE Livro (
    id_livro INT PRIMARY KEY,
    titulo VARCHAR(100),
    ano INT
);

CREATE TABLE Autor (
    id_autor INT PRIMARY KEY,
    nome VARCHAR(100)
);

CREATE TABLE Emprestimo (
    id_emprestimo INT PRIMARY KEY,
    data_emprestimo DATE,
    data_devolucao DATE,
    id_usuario INT NOT NULL,
    id_funcionario INT NOT NULL,

    FOREIGN KEY (id_usuario) REFERENCES Usuario(id_usuario),
    FOREIGN KEY (id_funcionario) REFERENCES Funcionario(id_funcionario)
);

-- TABELAS DE RELACIONAMENTO

-- EMPRESTIMO X LIVRO

CREATE TABLE Emprestimo_Livro (
    id_emprestimo INT,
    id_livro INT,

    PRIMARY KEY (id_emprestimo, id_livro),
    FOREIGN KEY (id_emprestimo) REFERENCES Emprestimo(id_emprestimo),
    FOREIGN KEY (id_livro) REFERENCES Livro(id_livro)
);

-- LIVRO X AUTOR

CREATE TABLE Livro_Autor (
    id_livro INT,
    id_autor INT,

    PRIMARY KEY (id_livro, id_autor),
    FOREIGN KEY (id_livro) REFERENCES Livro(id_livro),
    FOREIGN KEY (id_autor) REFERENCES Autor(id_autor)
);
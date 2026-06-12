drop database if exists pypo;
create database pypo;
use pypo;

create table Conquista(
 idConquista int primary key auto_increment,
 nome varchar(75),
 pontuacao int
);

CREATE TABLE Usuario 
( 
 senha VARCHAR(25) NOT NULL UNIQUE,  
 idUsuario INT PRIMARY KEY AUTO_INCREMENT,  
 email VARCHAR(45) NOT NULL UNIQUE,  
 nickname VARCHAR(25) NOT NULL UNIQUE, 
 pontuacao int
); 

CREATE TABLE UsuarioConquista (
 idUsuario INT,
 idConquista INT,
 PRIMARY KEY (idUsuario, idConquista),
 FOREIGN KEY (idUsuario) REFERENCES Usuario(idUsuario),
 FOREIGN KEY (idConquista) REFERENCES Conquista(idConquista)
);

CREATE TABLE Item 
( 
 idItem INT PRIMARY KEY AUTO_INCREMENT,  
 nome VARCHAR(25) NOT NULL,
 descricao TEXT NOT NULL,
 valor INT NOT NULL 
); 

insert into Item values
(default,"50/50","Reduz o número de opções para a metade",100);

CREATE TABLE Mundo 
( 
 idMundo INT PRIMARY KEY AUTO_INCREMENT,  
 linguagem VARCHAR(8) NOT NULL UNIQUE
); 

insert into Mundo values (default,"portugol");

CREATE TABLE Modulo 
( 
 idModulo INT PRIMARY KEY AUTO_INCREMENT,  
 numero INT NOT NULL,  
 nome VARCHAR(25) NOT NULL UNIQUE,
 idMundo int,
 foreign key (idMundo) references Mundo(idMundo)
); 

insert into Modulo values (default,1, "introdução",1);

CREATE TABLE Fase 
( 
 idFase INT PRIMARY KEY AUTO_INCREMENT,  
 MaterialApoio VARCHAR(99) NOT NULL,
 idModulo INT,  
 FOREIGN KEY(idModulo) REFERENCES Modulo(idModulo)
); 

insert into Fase values(default,"Pudim","1");


CREATE TABLE Exercicio 
( 
 titulo VARCHAR(25) NOT NULL UNIQUE,  
 Enunciado VARCHAR(99) NOT NULL UNIQUE,  
 alternativaA VARCHAR(99) NOT NULL,  
 alternativaB VARCHAR(99) NOT NULL,
 alternativaC VARCHAR(99) NOT NULL,
 alternativaD VARCHAR(99) NOT NULL,
 resposta CHAR(1) NOT NULL,  
 idExercicio INT PRIMARY KEY AUTO_INCREMENT,  
 numero INT,  
 idFase INT,
 FOREIGN KEY(idFase) REFERENCES Fase(idFase)
); 

insert into exercicio values("pudim","a","a","a","a","a","a",default,1,1);

CREATE TABLE Estoque 
( 
 qtd INT NOT NULL,  
 idUsuario INT,  
 idItem INT, 
 PRIMARY KEY(idUsuario, idItem),
 FOREIGN KEY(idUsuario) REFERENCES Usuario(idUsuario),
 FOREIGN KEY(idItem) REFERENCES Item(idItem)
); 

CREATE TABLE Progresso 
( 
 idUsuario INT,  
 idFase INT,
 PRIMARY KEY(idUsuario, idFase),
 FOREIGN KEY(idUsuario) REFERENCES Usuario(idUsuario),
 FOREIGN KEY(idFase) REFERENCES Fase(idFase)
); 

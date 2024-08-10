CREATE DATABASE fazenda;

USE fazenda;
CREATE TABLE cultura ( 
	culturaId int not null auto_increment,
	nome varchar(40) not null,
	primary key (culturaId)
);

CREATE TABLE praga (
	pragaId int not null auto_increment,
	nome varchar (40) not null,
	primary key (pragaId)
);

CREATE TABLE agrotoxico (
	agrotoxicoId int not null auto_increment,
	nome varchar (45) not null,
	descricao varchar(60) not null,
	und_med char(3) not null,
	quant_disp decimal (10,2),
	primary key (agrotoxicoId)
);

CREATE TABLE funcionario (
	funcId int not null auto_increment,
	nome varchar (40) not null,
	primary key (funcId)
);

CREATE TABLE areaPlantio (
	areaId int not null auto_increment,
	funcId int not null,
	culturaId int,
	tamanho varchar (10) not null,
    dataInicio date,
    dataMax date,
	primary key (areaId),
	foreign key (funcId) references funcionario (funcId),
	foreign key (culturaId) references cultura (culturaId)
);

CREATE TABLE pragaAgro (
	pragaId int not null,
	agrotoxicoId int not null,
	primary key (pragaId , agrotoxicoId),
    foreign key (pragaId) references praga (pragaId),
    foreign key (agrotoxicoId) references agrotoxico (agrotoxicoId)
);

CREATE TABLE estacao (
	estacaoId int not null auto_increment,
	nome varchar(20) not null,
	primary key (estacaoId)
);

CREATE TABLE pragaCultura (
	pragaId int not null,
    culturaId int not null,
    primary key (pragaId , culturaId),
    foreign key (pragaId) references praga (pragaId),
    foreign key (culturaId) references cultura (culturaId)
);

CREATE TABLE pragaCulturaFrequencia (
	estacaoId int not null,
	pragaId int not null,
    culturaId int not null,
	primary key (estacaoId , pragaId , culturaId),
    foreign key (estacaoId) references estacao (estacaoId),
    foreign key (pragaId) references pragaCultura (pragaId),
    foreign key (culturaId) references pragaCultura (culturaId)
);

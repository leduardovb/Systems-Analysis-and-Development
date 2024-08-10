CREATE TABLE medico(
	medicoId int not null auto_increment,
    nome varchar(45) not null,
    primary key(medicoId)
);

CREATE TABLE paciente(
	pacienteId int not null auto_increment,
    nome varchar(45) not null,
	primary key (pacienteId)
);

CREATE TABLE intervencao(
	intervencaoId  int not null auto_increment,
    descricao varchar(45) not null,
    primary key (intervencaoId)
);

CREATE TABLE consulta (
	consultaId int not null auto_increment,
    dataConsulta date not null,
    especialidadeId int,
    statuss varchar(45) not null,
    medicoId int not null,
    pacienteId int not null,
    primary key(consultaId , dataConsulta , medicoId , pacienteId),
    foreign key (medicoId) references medico (medicoId),
    foreign key (pacienteId) references paciente (pacienteId)
);

CREATE TABLE consultaIntervencao(
	consultaId int not null,
    intervencaoId int not null,
    primary key (consultaId , intervencaoId),
    foreign key (consultaId) references consulta (consultaId),
    foreign key (intervencaoId) references intervencao (intervencaoId)
);

CREATE TABLE exame(
	exameId int not null auto_increment,
    descricao varchar(45) not null,
    primary key (exameId)
);

CREATE TABLE especialidade(
	especialidadeId int not null auto_increment,
    descricao varchar(45) not null,
    primary key (especialidadeId)
);

CREATE TABLE especialidadeMedico(
	especialidadeId int not null,
    medicoId int not null,
    primary key (especialidadeId , medicoId),
    foreign key (especialidadeId) references especialidade (especialidadeId),
    foreign key (medicoId) references  medico (medicoId)
);

CREATE TABLE exameConsulta(
	exameId int not null,
    consultaId int not null,
    primary key (exameId , consultaId),
    foreign key (exameId) references exame (exameId),
    foreign key (consultaId) references consulta (consultaId)
);
